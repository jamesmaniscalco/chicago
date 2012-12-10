from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.utils import simplejson
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.template.loader import render_to_string

from chicago.gear.models import UserAccount, GearItem

import itertools


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


# return serialized list of all items in a user's possession
@dajaxice_register
def all_items(request):
    user = request.user     # grab user sending request...
    items_owned = GearItem.objects.filter(owner=user)   # list of gear items owned by the user
    items_loaned = GearItem.objects.filter(holder=user).exclude(owner=user) # list of gear items held (but not owned) by the user
    
    # concatenate two querysets
    items = itertools.chain(items_owned, items_loaned)
    
    # organize data into a dict for render_to_string
    data = {'items':items, 'user':request.user}
    
    # and return to browser as a string
    return render_to_string('gear/gear_items.json', data)
    

#checkout individual item
@dajaxice_register
def checkout_item(request, id):
    user = request.user     # get the user sending AJAX request
    # get the item of gear requested
    try:
        item = GearItem.objects.get(id=id)
    except DoesNotExist:    # if selected item does not exist in database, return error
        return simplejson.dumps({'status':'error', 'errors':['item does not exist']})
    if item.holder != user: # if selected item is not in request.user's possession, return error
        return simplejson.dumps({'status':'error', 'errors':['item not available for checkout']})
    if item.status == 'o':  # if item is already checked out, return error
        return simplejson.dumps({'status':'error', 'errors':['item already checked out']})
    
    # if all the above passes, checkout item and return success message
    item.status = 'o'
    item.save()
    return simplejson.dumps({'status':'success'})
        

#checkin individual item
@dajaxice_register
def checkin_item(request, id):
    user = request.user     # get the user sending AJAX request
    # get the item of gear requested
    try:
        item = GearItem.objects.get(id=id)
    except DoesNotExist:    # if selected item does not exist in database, return error
        return simplejson.dumps({'status':'error', 'errors':['item does not exist']})
    if item.holder != user: # if selected item is not in request.user's possession, return error
        return simplejson.dumps({'status':'error', 'errors':['item not available for checkin']})
    if item.status == 'i':  # if item is already checked out, return error
        return simplejson.dumps({'status':'error', 'errors':['item already checked in']})
    
    # if all the above passes, checkin item and return success message
    item.status = 'i'
    item.save()
    return simplejson.dumps({'status':'success'})
    
    
#retrieve an individual item, with its current status (for refreshing items in the browser, etc.)
@dajaxice_register
def get_item(request, id):
    # first, get the request user,
    user = request.user
    # then get the item.
    try:
        item = GearItem.objects.get(id=id)
    except DoesNotExist:    # if selected item does not exist in database, return error
        return simplejson.dumps({'status':'error', 'errors':['item does not exist']})
    if item.holder != user and item.owner != user:
        return simplejson.dumps({'status':'error', 'errors':['item only visible by its owner/holder']})
    
    # return the item's information to the browser
    items = [item]
    data = {'items':items, 'user':user}
    return render_to_string('gear/gear_items.json', data)

