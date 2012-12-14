from django.db.models import Q
from django.contrib.auth.models import User

from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from chicago.gear.models import UserAccount, GearItem

import itertools


# base class to make things compatible with Backbone
# (from http://paltman.com/2012/04/30/integration-backbonejs-tastypie/)
class BackboneCompatibleResource(ModelResource):
    class Meta:
        always_return_data = True


# custom Authentication to use Django's web authentication (from http://stackoverflow.com/a/8317498)
class WebAuthentication(BasicAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True
        else:
            return False
    def get_identifier(self, request):
        if request.user.is_authenticated():
            return request.user.username
        else:
            return super(WebAuthentication, self).get_identifier(request)


#### Resources

# resource for Users
class UserResource(BackboneCompatibleResource):
    class Meta:
        queryset = User.objects.all()
        include_resource_uri = False
        fields = ['username']
        

# API resource for gear items
class GearItemResource(BackboneCompatibleResource):
    # add owner and holder fields
    owner = fields.ForeignKey(UserResource, 'owner', full=True)
    holder = fields.ForeignKey(UserResource, 'holder', full=True)
    
    class Meta:
        authentication = WebAuthentication()  # require users to have a u/p pair
        authorization = DjangoAuthorization()   # limit viewable items to just those items viewable by a user

        queryset = GearItem.objects.all()

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        
        
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(Q(holder=request.user) | Q(owner=request.user))
