from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # This gets passed through views.details parameters
    # 
	# def details(request, word_id):
	# 	return HttpResponse("You are looking at word %s." % word_id)
    url(r'^(?P<word_id>[A-z]+)/$', views.details, name='details'),
    url(r'^[A-z]$', views.submit, name='submit'),
]
