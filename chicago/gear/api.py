from django.db.models import Q

from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

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
            return super(WebAuthentication, self).is_authenticated(request, **kwargs)
    def get_identifier(self, request):
        if request.user.is_authenticated():
            return request.user.username
        else:
            return super(WebAuthentication, self).get_identifier(request)


# API resource for gear items
class GearItemResource(BackboneCompatibleResource):
    class Meta:
        authentication = WebAuthentication()  # require users to have a u/p pair
        authorization = DjangoAuthorization()   # limit viewable items to just those items viewable by a user

        queryset = GearItem.objects.all()
        
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(Q(holder=request.user) | Q(owner=request.user))
