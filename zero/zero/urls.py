from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zero.views.home', name='home'),
    url(r'^', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEV:
    urlpatterns += patterns('', (r'^media/(.*)$', 'django.views.static.serve', {'document_root': './public/media'}),)
