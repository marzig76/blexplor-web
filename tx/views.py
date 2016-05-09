from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block, Tx, TxInput, TxOutput

def index(request):
    return HttpResponse("Transaction ID not specified")

def tx(request, tx):
    response = "Transaction: " + tx
    return HttpResponse(response)
