from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'(?P<slug>[\w-]+)$', board, name='board'),
)