# This is all of the views that the Microbug application supports

from django.shortcuts import render
from django.http import HttpResponse

# The main page
def index(request):
    return HttpResponse('Hello from Microbug')