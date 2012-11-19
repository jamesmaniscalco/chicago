from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.utils import simplejson
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# AJAX login method
@dajaxice_register
def login(request, form):
    f = AuthenticationForm(data=form)
    print f.is_valid()
    if f.is_valid():
        # if form validates, try to log user in
        username = f.cleaned_data['username']
        password = f.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                data = {'status':'Success!'}
            else:
                data = {'status':'Login failed - user not active'}
        else:
            data = {'status':'Login failed - no such username/password combination found.'}
    else:
        data = f.errors
    
    # return appropriate response
    return simplejson.dumps(data)

