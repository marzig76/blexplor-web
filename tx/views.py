from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Tx, TxInput, TxOutput


def index(request):
    message = "Transaction ID not specified"
    template = loader.get_template('blexplor_web/simple_message.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def tx(request, tx):
    try:
        txs = Tx.objects.filter(tx_hash=tx)
        inputs = TxInput.objects.filter(tx_id__in=txs)
        outputs = TxOutput.objects.filter(tx_id__in=txs)

        template = loader.get_template('tx/index.html')
        context = {
            'txs': txs,
            'inputs': inputs,
            'outputs': outputs,
            }
        return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        return HttpResponse("Block does not exist")
