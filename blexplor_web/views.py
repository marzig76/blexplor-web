from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from block.models import Block

def index(request):
    blocks = Block.objects.all().order_by('-block_height')[:10]

    template = loader.get_template('blexplor_web/index.html')
    context = {
        'blocks': blocks,
    }
    return HttpResponse(template.render(context, request))
