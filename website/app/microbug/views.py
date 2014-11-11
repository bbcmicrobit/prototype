# This is all of the views that the Microbug application supports

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import settings
import sys
from primary_version_store import PrimaryVersionStore
from pending_version_store import PendingVersionStore
from microbug.models import Version

# Get a version store we can keep uploaded files in.
primary_version_store = PrimaryVersionStore(settings.PRIMARY_STORE_DIRECTORY)
pending_queue_store = PendingVersionStore(settings.PENDING_QUEUE_DIRECTORY)

# Get the logger for these views
logger = logging.getLogger(__name__)

# The main page
def index(request):
    return render(request, 'microbug/index.html', {})

# Called when the user clicks the 'build_code' button in the editor.
@csrf_exempt
def build_code(request):
    try:
        # Check we're a POST request
        if request.method != 'POST':
            return HttpResponseBadRequest('Must be a POST request')

        # Grab the JSON from the request body and make it nicer
        try:
            json_obj = json.loads(request.body)
            pretty_json = _prettify_json(json_obj)
        except ValueError:
            logger.error("Build_code could not process Json: %s" % str(request))
            return HttpResponse("Could not process request, not a valid Json object?")

        # Extract the name from the form fields
        if 'program_name' in json_obj['repr']:
            program_name = json_obj['repr']['program_name']
        else:
            program_name = None

        # Write it to both of the stores
        (numeric_id, random_uuid) = primary_version_store.write_new_version(pretty_json)
        python_code = json_obj['repr']['code']
        pending_queue_store.write_new_version(python_code, numeric_id, random_uuid)

        # Write it to the database
        version = Version(id=numeric_id, name=program_name, store_uuid=random_uuid)
        version.save()

        return HttpResponse('Hello World: {0}-{1}: {2}\n{3}'.format(numeric_id, random_uuid, str(pretty_json), python_code))

    except BytesWarning:
        e = sys.exc_info()[0]
        logger.exception(e)
        return HttpResponse('Danger: %s' % e)

# Convert JSON to a prettified version
def _prettify_json(json_obj):
    return json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))