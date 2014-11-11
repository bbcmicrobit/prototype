# This is all of the views that the Microbug application supports

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import settings
import sys
from primary_version_store import PrimaryVersionStore
from pending_version_store import PendingVersionStore

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
        json_obj = json.loads(request.body)
        pretty_json = _prettify_json(json_obj)

        # Write it to both of the stores
        (numeric_id, random_uuid) = primary_version_store.write_new_version(pretty_json)
        python_code = json_obj['repr']['code']
        pending_queue_store.write_new_version(python_code, numeric_id, random_uuid)

        return HttpResponse('Hello World: {0}-{1}: {2}\n{3}'.format(numeric_id, random_uuid, str(pretty_json), python_code))

    except BytesWarning:
        e = sys.exc_info()[0]
        logger.exception(e)
        return HttpResponse('Danger: %s' % e)

# Convert JSON to a prettified version
def _prettify_json(json_obj):
    return json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))