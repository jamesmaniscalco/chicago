from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# import Dajaxice
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()


urlpatterns = patterns('',
    url(r'^gear/', include('chicago.gear.urls')),
    url(r'^$', 'chicago.gear.views.default'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # login url
    url(r'^login/', 'chicago.gear.views.login'),
    url(r'logout/', 'chicago.gear.views.logout'),

    # enable Dajaxice
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
