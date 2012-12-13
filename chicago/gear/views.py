# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.contrib.auth.models import User, Group

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()


#login view
def login(request):
    form = AuthenticationForm()
    return render_to_response('gear/login_form.html', {'form':form}, context_instance=RequestContext(request))
    

#logout view
def logout(request):
    return HttpResponse('Successfully logged out.')


#default home view for app
@login_required
def default(request):
    return render_to_response('gear/home.html', context_instance=RequestContext(request))
    

#list of items associated with the user
@login_required
def items(request):
    return render_to_response('gear/items.html', context_instance=RequestContext(request))



