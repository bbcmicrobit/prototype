# This is all of the views that the Microbug application supports

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import settings
import sys
from primary_version_store import PrimaryVersionStore
from pending_version_store import PendingVersionStore
from microbug.models import Program, Version
import re

# Get a version store we can keep uploaded files in.
primary_version_store = PrimaryVersionStore(settings.PRIMARY_STORE_DIRECTORY)
pending_queue_store = PendingVersionStore(settings.PENDING_QUEUE_DIRECTORY)

# Get the logger for these views
logger = logging.getLogger(__name__)

# The main page
def index(request):
    return render(request, 'microbug/index.html', {})

# Create a new program
def create_program(request):
    return render(request, 'microbug/create_program.html', {'programs': programs})

# View a single program
def program(request, program_id):
    viewed_program = get_object_or_404(Program, pk=program_id)
    return render(request, 'microbug/program.html', {'program': viewed_program})

# List all of the Programs available on the system
def programs(request):
    programs = Program.objects.all()
    return render(request, 'microbug/programs.html', {'programs': programs})

# Show the tutorials
def tutorial(request, tutorial_name, page_number=1):
    return render(request, 'microbug/tutorial_multiple_toolboxes.html', {})

##########################################

# Called when the user clicks the 'build_code' button in the editor.
@csrf_exempt
def build_code(request):
    # Check we're a POST request
    if request.method != 'POST':
        return HttpResponseBadRequest('Must be a POST request')

    # Grab the JSON from the request body and make it nicer
    try:
        json_obj = json.loads(request.body)
        pretty_json = _prettify_json(json_obj)
    except ValueError:
        logger.error("Build_code could not process Json: %s" % str(request))
        return HttpResponseBadRequest("Could not process request, not a valid Json object?")

    # Count the number of lines of code
    python_code = json_obj['repr']['code']
    lines_of_code = _count_lines(python_code)

    # Write it to both of the stores
    (numeric_id, random_uuid) = primary_version_store.write_new_version(pretty_json)
    pending_queue_store.write_new_version(python_code, numeric_id, random_uuid)

    # Write the Version to the database
    version = Version(id=numeric_id, store_uuid=random_uuid, lines_of_code_count=lines_of_code)
    version.save()

    # Write the Program to the database
    program_name = json_obj['program_name']
    new_program = Program(version=version, name=program_name)
    new_program.save()

    # Return the program's ID
    return HttpResponse(str(new_program.id))

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

    # Perform the actual rename
    target_program = get_object_or_404(Program, pk=json_obj['program_id'])
    target_program.name = json_obj['program_name']
    target_program.save()

    return HttpResponse('Renamed successfully')

# Convert JSON to a prettified version
def _prettify_json(json_obj):
    return json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))

# Counts the number of lines in a piece of text
def _count_lines(text):
    return len(re.split('[\n\r]+', text))-1