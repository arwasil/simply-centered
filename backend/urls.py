from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('api.views',
    url(r'^$', list, name="home"),
    url(r'bundle/(?P<id>.+)/$', bundle, name="bundle"),
)
