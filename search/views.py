from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block
from django.http import HttpResponseRedirect

def index(request):
    search = request.GET['search']
    if search != '':
        if search.isnumeric():
            return HttpResponseRedirect("/block/" + search)
        else:
            response = 'Address: ' + search
    else:
        response = 'No search parameter provided.'

    return HttpResponse(response)

def search_string(request, search_string):
    return HttpResponse("Search string: " + search_string)
