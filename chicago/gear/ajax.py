from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.utils import simplejson
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


#test ajax function for learning DAJAX
@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello, World!'})

