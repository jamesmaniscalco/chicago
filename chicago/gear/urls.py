from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chicago.views.home', name='home'),
    url(r'^$/', 'chicago.gear.views.default'),
    url(r'login/', 'chicago.gear.views.login'),
)