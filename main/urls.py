from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'(?P<name>[\w-]+)$', board, name='board'),
)