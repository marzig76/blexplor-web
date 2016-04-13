from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block, Tx, TxInput, TxOutput

def index(request):
    return HttpResponse("Address not specified")

def address(request, address):
    template = loader.get_template('address/index.html')
    context = {
        'address': address,
    }
    return HttpResponse(template.render(context, request))

