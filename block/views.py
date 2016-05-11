from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from block.models import Block, Tx, TxInput, TxOutput


def index(request):
    message = "Block not specified"
    template = loader.get_template('blexplor_web/simple_message.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def height(request, height):
    try:
        b = Block.objects.get(block_height=height)
        txs = Tx.objects.filter(block_id=b.id)
        inputs = TxInput.objects.filter(tx_id__in=txs)
        outputs = TxOutput.objects.filter(tx_id__in=txs)

        template = loader.get_template('block/index.html')
        context = {
            'b': b,
            'txs': txs,
            'inputs': inputs,
            'outputs': outputs,
            }
        return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        return HttpResponse("Block does not exist")
