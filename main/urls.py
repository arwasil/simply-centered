from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'([\w-]+)/([\w-]+)/([\w-]+)$', board),
    url(r'([\w-]+)/([\w-]+)$', board),
    url(r'([\w-]+)$', board, name='board'),
   
)