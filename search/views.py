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
        elif len(search) == 34:
            return HttpResponseRedirect("/address/" + search)
        else:
            return HttpResponseRedirect("/tx/" + search)
    else:
        message = "No search parameter provided."
        template = loader.get_template('blexplor_web/simple_message.html')
        context = {
            'message': message,
        }
        return HttpResponse(template.render(context, request))
