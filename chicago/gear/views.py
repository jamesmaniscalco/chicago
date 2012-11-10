# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.auth.models import User, Group


#login view
def login(request):
    # simple return, doesn't do anything yet
    return HttpResponse('Login page')#, context_instance=RequestContext(request))
    
#login processor with AJAX
def login_submit(request):
    return HttpRequest('Login submitted')


# @login_required
# def default(