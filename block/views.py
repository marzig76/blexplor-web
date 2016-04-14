from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block, Tx, TxInput, TxOutput

def index(request):
    return HttpResponse("Block not specified")

def height(request, height):
    b = Block.objects.get(block_height=height)
    txs = Tx.objects.filter(block_id=b.id)

    template = loader.get_template('block/index.html')
    context = {
        'b': b,
        'txs': txs,
    }
    return HttpResponse(template.render(context, request))

