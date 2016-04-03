from django.shortcuts import render
from time import gmtime, strftime
import json

def index(request):
    return render(request, 'engine/hello.html', {})