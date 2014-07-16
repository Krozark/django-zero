from django.conf.urls import patterns, include, url

from website.views import HomeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^/$', 'zero.views.home', name='home'),
)
