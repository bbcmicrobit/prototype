# This is all of the views that the Microbug application supports

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get the logger for these views
logger = logging.getLogger(__name__)

# The main page
def index(request):
    return render(request, 'microbug/index.html', {})

# Called when the user clicks the 'build_code' button in the editor.
@csrf_exempt
def build_code(request):
    request_json = json.loads(request.body)
    request_python = request_json['repr']['code']
    request_xml = request_json['repr']['xml']
    pretty_json = json.dumps(request_json, sort_keys=True, indent=4, separators=(',', ': '))

    logger.debug("JSON: %s" % pretty_json)
    logger.debug("XML: %s" % request_xml)
    logger.debug("CODE: %s" % request_python)

    return HttpResponse('Hello World')