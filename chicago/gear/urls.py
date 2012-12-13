from django.conf.urls import patterns, include, url

from tastypie.api import Api

from chicago.gear.api import GearItemResource


# initialize API resources
v1_api = Api(api_name='v1')
v1_api.register(GearItemResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicago.views.home', name='home'),
    url(r'^/', 'chicago.gear.views.default'),
    url(r'login/', 'chicago.gear.views.login'),
    url(r'logout/', 'chicago.gear.views.logout'),
    url(r'items/', 'chicago.gear.views.items'),
    url(r'api/', include(v1_api.urls)),
)
