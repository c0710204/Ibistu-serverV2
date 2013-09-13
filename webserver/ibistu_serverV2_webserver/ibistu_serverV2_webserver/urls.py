from django.conf.urls import patterns, include, url
from webserver.views import hello,hello1
import webserver
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibistu_serverV2_webserver.views.home', name='home'),
    # url(r'^ibistu_serverV2_webserver/', include('ibistu_serverV2_webserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/api.php',webserver.views.api),
    url(r'^test',webserver.views.memcache_testbuilder)
)
