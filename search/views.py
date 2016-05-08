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
            return HttpResponseRedirect("/address/" + search)
    else:
        return HttpResponse('No search parameter provided.')
