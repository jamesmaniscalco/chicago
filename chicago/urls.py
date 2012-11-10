from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicago.views.home', name='home'),
    url(r'^gear/', include('chicago.gear.urls')),
    url(r'^$/', 'chicago.gear.views.default'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # login url
    url(r'^login/', 'chicago.gear.views.login'),
)
