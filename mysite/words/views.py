from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Rack

import Unscrabble
# Create your views here.
# def index(request):
# 	list_of_entered_words = Rack.objects.all()
# 	template = loader.get_template('words/index.html')
# 	context = {
# 		'list_of_entered_words': list_of_entered_words,
# 	}
# 	return HttpResponse(template.render(context, request))

def index(request):
    list_of_entered_words = Rack.objects.all()
    context = {'list_of_entered_words': list_of_entered_words}
    # render( request, template, dictionary )
    return render(request, 'words/index.html', context)

def details(request, word_id):
	# return HttpResponse("You are looking at word %s." % word_id)
	context = {'word': word_id}
	return render(request, 'words/details.html', context)

def submit(request):
	# return HttpResponse("You are looking at word %s." % word_id)
	unscrab = Unscrabble.main(request.POST.get("entered_word"), 'v')

	context = {'word': request.POST.get("entered_word"),
				'unscrab': unscrab
	}
	
	Rack.objects.get_or_create(entered_word=request.POST.get("entered_word"))

	return render(request, 'words/submit.html', context)

