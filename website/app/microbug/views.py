# This is all of the views that the Microbug application supports

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseServerError, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import settings
import sys
from compiled_version_store import CompiledVersionStore
from primary_version_store import PrimaryVersionStore
from pending_version_store import PendingVersionStore
from microbug.models import Program, Tutorial, UserProfile, Version, FacilitatorRequest
import re
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.contrib import auth
from django.contrib.auth.models import User
import pprint
import datetime
import random_phrase_generator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Get a version store we can keep uploaded files in.
compiled_version_store = CompiledVersionStore(settings.COMPILED_PYTHON_PROGRAMS_DIRECTORY)
primary_version_store = PrimaryVersionStore(settings.PRIMARY_STORE_DIRECTORY)
pending_queue_store = PendingVersionStore(settings.PENDING_PYTHON_QUEUE_DIRECTORY)

# Get the logger for these views
logger = logging.getLogger(__name__)
#raise Exception(str(logger))

# The main page
def index(request):
    logger.warn("INDEX HASH: {0}".format(_add_defaults(request)))

    return render(
        request, 'microbug/index.html',
        _add_defaults(request)
    )

# Create a new program
def create_program(request):
    return render(
        request, 'microbug/create_program.html',
        _add_defaults(request, {'programs': programs})
    )

# Shows the 'create user' form
def create_user_form(request):
    return render(
        request, 'microbug/create_user.html',
        _add_defaults(request, {})
    )

# View a single program
def program(request, program_id):
    viewed_program = get_object_or_404(Program, pk=program_id)
    (user, user_profile) = _user_and_profile_for_request(request)
    # TODO: This needs tweaking.
    owns_program = _owns_program(request, user_profile, viewed_program)
    return render(
        request, 'microbug/program.html',
        _add_defaults(request, {
            'program': viewed_program,
            'owns_program': owns_program
        })
    )

# List all of the Programs available on the system
def programs(request):
    programs = Program.objects.all()
    return render(
        request, 'microbug/programs.html',
        _add_defaults(request,{'programs':programs})
    )

# Show a specific tutorial
def tutorial(request, tutorial_name, page_number=1):
    tutorial_obj = get_object_or_404(Tutorial, name=tutorial_name)
    return render(
        request, 'microbug/tutorial.html',
        _add_defaults(request, {'tutorial_content': mark_safe(tutorial_obj.content)})
    )

# Show a list of all of the tutorials available in the system
def tutorials(request):
    tutorials = Tutorial.objects.all()
    return render(
        request, 'microbug/tutorials.html',
        _add_defaults(request, {'tutorials':tutorials})
    )

# Display the details for a user
def user(request, user_id):
    viewed_user = get_object_or_404(User, pk=user_id)
    (user, user_profile) = _user_and_profile_for_request(request)
    viewed_user_profile = saved_profile_for_user(viewed_user)

    # Must be logged in
    if not user:
        return HttpResponseNotAllowed("Must be logged in to view user details")

    if viewed_user==user or user_profile.is_facilitator_of(viewed_user_profile):
        return render(
            request, 'microbug/user.html',
            _add_defaults(request, {
                'viewed_user': viewed_user,
                'viewed_user_profile': viewed_user_profile,
                'viewing_own_details': user == viewed_user,
                'viewing_facilitated_child_details': user_profile is not None and user_profile.is_facilitator_of(viewed_user)
            })
        )
    else:
        return HttpResponseNotAllowed("Only the user and their facilitators can view this page")

# Show the page to register a user
def register_user(request):
    return render(
        request, 'microbug/register_user.html',
        _add_defaults(request)
    )

# Downloads a compiled .hex program
def download(request, program_id, program_name=None):
    program = get_object_or_404(Program, pk=program_id)

    # Program name defaults to the name in the DB.
    if program_name is None:
        program_name = program.name

    # Obtain the data from the compiled store, if it's not there then return a HTTP
    # error
    content = compiled_version_store.hex(program.version.base_filename())
    if content is None:
        return HttpResponseNotFound("No compiled version found")

    response = HttpResponse(content, content_type='application/octet-stream')
    saved_filename = "%s.hex" % slugify(program_name)
    logger.debug("Saving as '{0}'".format(saved_filename))

    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(saved_filename)

    return response

##########################################

# Called when a user tries to log in
@csrf_exempt
def authenticate_user(request):
    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")
    username = json_obj['username']
    password = json_obj['password']

    user = auth.authenticate(username=username, password=password)
    if user is None:
        response_obj = {"status": "invalid"}
        logger.info("Invalid login attempt for '{0}'".format(username))
    else:
        response_obj = {"status": "authenticated", "username": user.username}
        auth.login(request, user)
        _claim_unattributed_items(request)
        logger.info("Login successful for '{0}'".format(username))

        # Clear the 'has_pending_password_request' flag
        user_profile = saved_profile_for_user(user)
        if user_profile.has_pending_password_request:
            user_profile.has_pending_password_request = False
            user_profile.save()

    logger.info(response_obj)
    return HttpResponse(json.dumps(response_obj))

# Called when the user clicks the 'build_code' button in the editor.
@csrf_exempt
def build_code(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # Reserve the ID for the primary store
    (numeric_id, random_uuid) = primary_version_store.reserve_new_id()

    # Count the number of lines of code
    python_code = json_obj['repr']['code']
    lines_of_code = _count_lines(python_code)

    # Pull out program details from request
    program_name = json_obj['program_name']
    program_id = json_obj['program_id']

    # We're going to need a user and a user profile
    (user, user_profile) = _user_and_profile_for_request(request)

    # Check if we've been provided with a Program ID, if so find the program now so we can
    # maintain the version links
    new_program = None
    if program_id:
        new_program = get_object_or_404(Program, pk=program_id)

        # Check we can create the program
        not_owns_program = not _owns_program(request, user_profile, new_program)
        if not_owns_program and json_obj['edit_phrase'] != new_program.edit_phrase:
            return HttpResponseNotAllowed('You do not have permission to edit that program')
        logger.warn("Authenticated")

    # Write the new Version to the database
    version = Version(
        id=numeric_id, store_uuid=random_uuid,
        program=new_program, lines_of_code_count=lines_of_code,
        owner = user_profile
    )
    if new_program:
        version.program = new_program
        new_program.version = version
        version.previous_version = new_program.version
        json_obj['previous_version'] = new_program.version.id
        new_program.save()

    version.owner = user_profile
    version.save()

    # If we didn't obtain a Program from the ID we'll create one now, if we did we'll update it
    # to point to new version
    if new_program:
        created_program = False
        new_program.name = program_name
        new_program.save()
    else:
        created_program = True
        new_program = Program(version=version, name=program_name, owner=user_profile)
        new_program.save()
        # We also need to update version
        version.program = new_program
        version.save()

    # Add the program details to the JSON
    json_obj['program_id'] = new_program.id

    # Write it to both of the stores
    logger.debug("JSON: {0}".format(json_obj));

    pretty_json = _prettify_json(json_obj)
    primary_version_store.write_new_version(pretty_json, numeric_id, random_uuid)
    pending_queue_store.write_new_version(python_code, numeric_id, random_uuid)

    # If we're not logged in we'll store the IDs of the new stuff in the session.
    if user_profile is None:
        # Check we have the two stores in the session.
        session = request.session
        if 'unattributed_programs' not in session:
             session['unattributed_programs'] = []
        if 'unattributed_versions' not in session:
            session['unattributed_versions'] = []

        # Add the newly created items
        unattributed_versions = session['unattributed_versions']
        unattributed_versions.append(version.id)
        session['unattributed_versions'] = unattributed_versions
        if created_program:
            unattributed_programs = session['unattributed_programs']
            unattributed_programs.append(new_program.id)
            session['unattributed_programs'] = unattributed_programs

    # Return the program's ID
    return HttpResponse(str(new_program.id))

# Used by a facilitator to request a password reset.
@csrf_exempt
def confirm_password_reset(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")


    # Find the user
    child = get_object_or_404(User, pk=json_obj['id'])
    child_profile = saved_profile_for_user(child)

    # Check there's a request pending
    if not child_profile.has_pending_password_request:
        return HttpResponseNotAllowed("There's no pending request")

    # Request must be by the facilitator
    (user, user_profile) = _user_and_profile_for_request(request)
    if not user_profile.is_facilitator_of(child):
        return HttpResponseNotAllowed("This can only be done by the child's facilitator")

    # Change the user's password
    password = random_phrase_generator.random_password()
    child.set_password(password)
    child.save()

    # Clear the request
    child_profile.has_pending_password_request = False
    child_profile.save()

    # Return the user details in a JSON obj.
    json_obj = {
        "username": child.username, "password": password, "id": child.id
    }
    return HttpResponse(json.dumps(json_obj))

# Creates a new user and returns the details
@csrf_exempt
def create_user(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Create the new user
    username = random_phrase_generator.random_username()
    password = random_phrase_generator.random_password()
    new_user = User(username=username)
    new_user.set_password(password)
    new_user.save()

    # Return the user details in a JSON obj.
    json_obj = {
        "username": username, "password": password, "id": new_user.id
    }
    return HttpResponse(json.dumps(json_obj))


# Records that a user has made a request for someone else to be their facilitator
@csrf_exempt
def facilitator_request(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # We're going to need a user and a user profile
    (user, user_profile) = _user_and_profile_for_request(request)

    # Check we're logged in
    if user is None:
        res = HttpResponse("You must be logged in")
        res.status_code = 401
        return res

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # # Extract the facilitator, checking we find them.
    facilitator_name = json_obj['facilitator_name']
    logger.warn("NAME: "+facilitator_name)
    facilitator = get_object_or_404(User, username=facilitator_name)
    facilitator_profile = saved_profile_for_user(facilitator)

    # # Make sure the facilitator is valid
    if facilitator == user:
        # // Lorem ipsum
        return HttpResponse('You cannot be your own facilitator.', None, 405)
    if not facilitator_profile.is_facilitator():
        # // Lorem ipsum
        return HttpResponse('That person is not a facilitator.', None, 405)
    if FacilitatorRequest.objects.filter(child=user, facilitator=facilitator, is_pending=True).exists():
        # // Lorem ipsum
        return HttpResponse('You already have a request for them.', None, 405)
    if facilitator_profile.is_facilitator_of(user):
        # // Lorem ipsum
        return HttpResponse('That person is already your facilitator.', None, 405)

    # Make the actual requestaj
    _make_authenticated_facilitator_request(user, facilitator)

    return HttpResponse("Request sent")

# Copies a program to produce a new version
@csrf_exempt
def fork_code(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # We're going to need to know if we have a user.
    (user, user_profile) = _user_and_profile_for_request(request)

    # Find the program, change the ownership details, clear the PK (Forces the DB
    #  to save as a new program), and save it
    src_id = json_obj['src_id']

    program = get_object_or_404(Program, pk=src_id)
    program.pk = None
    program.owner = user_profile
    program.edit_phrase = random_phrase_generator.random_edit_phrase()
    program.save()

    # If we're not logged in we'll store the IDs of the new program.
    if user_profile is None:
        # Check we have the two stores in the session.
        session = request.session
        if 'unattributed_programs' not in session:
             session['unattributed_programs'] = []

        # Add the newly created item
        unattributed_programs = session['unattributed_programs']
        unattributed_programs.append(program.id)
        session['unattributed_programs'] = unattributed_programs


    json_obj = {
        'src_id': src_id,
        'fork_id': program.id
    }
    return HttpResponse(json.dumps(json_obj))

# Returns the HTML for the login pane based on whether the user is logged in or not
@csrf_exempt
def login_pane(request):
    return render(
        request, 'microbug/partials/_login_pane.html',
        _add_defaults(request)
    )

# Return the status of the program specified
def queue_status(request, program_id):
    queried_program = get_object_or_404(Program, pk=program_id)
    if (queried_program.version is None):
        json_obj = {
            'status': 'no_version',
            'id': program_id,
        }
    elif (queried_program.version.is_compiled()):
        json_obj = {
            'status': 'compiled',
            'id': program_id,
            'version': queried_program.version.id,
        }
    else:
        json_obj = {
            'status': 'in_compile_queue',
            'id': program_id,
            'version': queried_program.version.id,
            'eta': str(queried_program.version.python_compilation_eta()),
        }
    return HttpResponse(json.dumps(json_obj))

# Rename a program at the user's request
@csrf_exempt
def rename_program(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("Rename_Program could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # Find the request
    target_program = get_object_or_404(Program, pk=json_obj['program_id'])

    # Check we're the owner of the program
    (user, user_profile) = _user_and_profile_for_request(request)
    if target_program.owner != user_profile:
        res = HttpResponse("This is not your program")
        res.status_code = 403
        return res

     # Perform the actual rename
    target_program.name = json_obj['program_name']
    target_program.save()

    return HttpResponse('Renamed successfully')


# Records that the user has requested a password reset
@csrf_exempt
def request_password_reset(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("respond_to_facilitator_request could not process Json: {}".format(str(request)))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # Find the user and mark them for password resets.
    user = get_object_or_404(User, username=json_obj['username'])
    user_profile = saved_profile_for_user(user)
    user_profile.has_pending_password_request = True
    user_profile.save()

    # TODO: SEND FACILITATOR EMAILS HERE.

    return HttpResponse('Request made')


# Reply the a facilitator request as a facilitator
@csrf_exempt
def respond_to_facilitator_request(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("respond_to_facilitator_request could not process Json: {}".format(str(request)))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")
    request_id = json_obj['request_id']
    is_accepted = json_obj['is_accepted']

    # Find the request
    facilitator_request = get_object_or_404(FacilitatorRequest, pk=request_id)

    # Check we're the facilitator
    (user, user_profile) = _user_and_profile_for_request(request)
    if facilitator_request.facilitator != user:
        res = HttpResponse("This is not your request")
        res.status_code = 403
        return res

    # Get the child for the request
    child = facilitator_request.child
    child_profile = saved_profile_for_user(child)

    # Everything seems accepted, add the Facilitator.
    if is_accepted:
        child_profile.facilitators.add(user_profile)

    # We've finished with the request, update it and save it.
    facilitator_request.is_pending = False
    facilitator_request.was_accepted = is_accepted
    facilitator_request.resolved_at = datetime.datetime.now()
    facilitator_request.save()

    return HttpResponse("Okay")

# Update the user's details
@csrf_exempt
def update_user_details(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # We're going to need a user and a user profile
    (user, user_profile) = _user_and_profile_for_request(request)

    # User needs to be logged in
    if user is None:
        return HttpResponseNotAllowed("You need to be logged in")

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("respond_to_facilitator_request could not process Json: {}".format(str(request)))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # Handle email address
    if 'email' in json_obj and user_profile.is_facilitator:
        email_address = json_obj['email'].strip()
        if email_address is not None and email_address != '':
            try:
                validate_email(email_address)
            except ValidationError as e:
                res = HttpResponse("Invalid email address")
                res.status_code = 400
                return res
            user_profile.email = email_address
        else:
            user_profile.email = None

    # Update the facility
    user_profile.realname = json_obj['name']
    answers = json_obj['question_answers']
    user_profile.question_1  = answers[0]
    user_profile.question_2  = answers[1]
    user_profile.question_3  = answers[2]
    user_profile.question_4  = answers[3]
    user_profile.question_5  = answers[4]
    user_profile.question_6  = answers[5]
    user_profile.question_7  = answers[6]
    user_profile.question_8  = answers[7]
    user_profile.question_9  = answers[8]
    user_profile.question_10 = answers[9]
    user_profile.save()

    return HttpResponse("Updated")

# Sets the user's email
@csrf_exempt
def set_email(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # We're going to need a user and a user profile
    (user, user_profile) = _user_and_profile_for_request(request)

    # User needs to be logged in
    if user is None:
        return HttpResponseNotAllowed("You need to be logged in")

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
    except ValueError:
        logger.error("respond_to_facilitator_request could not process Json: {}".format(str(request)))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # This needs to be a valid email address
    email_address = json_obj['email']
    try:
        validate_email(email_address)
    except ValidationError as e:
        res = HttpResponse("Invalid email address")
        res.status_code = 400
        return res

    # Set the user's email address and save it
    user_profile.email = email_address
    user_profile.save()
    logger.warn("Set email for user "+str(user_profile.id)+" to "+user_profile.email)

    return HttpResponse("Email updated")

# Signs the user out of the system
@csrf_exempt
def sign_out(request):
    auth.logout(request)
    return HttpResponse("Logged out")

# Assigns ownership of unattributed items in the session
def _claim_unattributed_items(request):
    session = request.session
    (user, user_profile) = _user_and_profile_for_request(request)

    if 'unattributed_programs' in session:
        for program_id in session['unattributed_programs']:
            try:
                program = Program.objects.get(pk=program_id)
                program.owner = user_profile
                program.save()
            except Program.DoesNotExist:
                logger.error("Could not find program with ID {} from unattributed session")
        for version_id in session['unattributed_versions']:
            try:
                version = Version.objects.get(pk=version_id)
                version.owner = user_profile
                version.save()
            except Version.DoesNotExist:
                logger.error("Could not find version with ID {} from unattributed session")

    session['unattributed_programs'] = []
    session['unattributed_versions'] = []

# Convert JSON to a prettified version
def _prettify_json(json_obj):
    return json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))

# Counts the number of lines in a piece of text
def _count_lines(text):
    return len(re.split('[\n\r]+', text))-1


# Combines the hash provided with the default hash for the request to return a combined total.
def _add_defaults(request, content=None):
    if content is None:
        content = {}

    (db_user, user_profile) = _user_and_profile_for_request(request)
    if 'unattributed_programs' not in request.session:
        request.session['unattributed_programs'] = []
    if 'unattributed_versions' not in request.session:
        request.session['unattributed_versions'] = []

    if user_profile and user_profile.is_facilitator():
        is_facilitator = True
    else:
        is_facilitator = False

    # Check if we're logged in as a faciliator without an email address set.
    if is_facilitator:
        current_email = user_profile.email
        if current_email is None or current_email == '':
            needs_facilitator_email = True
        else:
            needs_facilitator_email = False
    else:
        needs_facilitator_email = False

    if db_user is not None:
        logger.warn(db_user.username+
                    ": Fac "+str(is_facilitator)+
                    ", Email "+str(needs_facilitator_email)
        )

    content.update({
        'user': db_user,
        'user_profile': user_profile,
        'needs_facilitator_email': needs_facilitator_email,

        'session_content': pprint.pformat(request.session),
        'unattributed_programs': request.session['unattributed_programs'],
        'unattributed_versions': request.session['unattributed_versions']
    })
    return content


# Returns a saved profile for the user
def saved_profile_for_user(user):
    if not user.pk:
        user.save()
    (user_profile, user_profile_created) = UserProfile.objects.get_or_create(pk=user.id, user=user)
    if user_profile_created:
        user_profile.save()
    return user_profile

# Returns a tuple containing the user and profile from the request, or (None, None) if
# they don't exist
def _user_and_profile_for_request(request):
    if request.user.is_authenticated():
        db_user = request.user
        user_profile = saved_profile_for_user(db_user)
    else:
        db_user = None
        user_profile = None
    logger.warn("User details: {0} / {1}".format(db_user, user_profile))
    return db_user, user_profile

# After everything is confirmed this makes a facilitator request
def _make_authenticated_facilitator_request(user, facilitator):
    logger.warn("*** Confirmed facilitator request from '{}' to '{}'".format(user.username, facilitator.username))
    request = FacilitatorRequest(child=user, facilitator=facilitator)
    request.save()

# Returns a boolean indicating whether the user provided owns the program provided
def _owns_program(request, user_profile, program):
    if user_profile is None:
        # They own it if they have it in their pending programs
        session = request.session
        if 'unattributed_programs' in session:
            return program.id in session['unattributed_programs']
        else:
            return False
    else:
        # They own it if they are the owner
        return program.owner == user_profile

