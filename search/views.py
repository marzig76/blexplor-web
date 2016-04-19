from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("No search parameter specified")

def search_string(request, search_string):
    return HttpResponse("Search string: " + search_string)
