from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block, Tx, TxInput, TxOutput


def index(request):
    message = "Address not specified"
    template = loader.get_template('blexplor_web/simple_message.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def address(request, address):
    inputs = TxInput.objects.filter(addr=address)
    outputs = TxOutput.objects.filter(addr=address)

    template = loader.get_template('address/index.html')
    context = {
        'address': address,
        'inputs': inputs,
        'outputs': outputs,
    }
    return HttpResponse(template.render(context, request))
