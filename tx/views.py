from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block, Tx, TxInput, TxOutput


def index(request):
    message = "Transaction ID not specified"
    template = loader.get_template('blexplor_web/simple_message.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def tx(request, tx):
    response = "Transaction: " + tx
    return HttpResponse(response)
