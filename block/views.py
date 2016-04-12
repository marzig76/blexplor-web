from django.shortcuts import render
from django.http import HttpResponse
from block.models import Block, Tx, TxInput, TxOutput

def index(request):
    return HttpResponse("Block not specified")

def height(request, height):
    b = Block.objects.get(block_height=height)
    return HttpResponse(b)
