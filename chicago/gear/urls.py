from django.conf.urls import patterns, include, url
from chicago.gear.api import GearItemResource

# initialize API resources
gear_item_resource = GearItemResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicago.views.home', name='home'),
    url(r'^/', 'chicago.gear.views.default'),
    url(r'login/', 'chicago.gear.views.login'),
    url(r'items/', 'chicago.gear.views.items'),
    url(r'api/', include(gear_item_resource.urls)),
)
