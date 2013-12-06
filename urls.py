from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main.views.index', name='index'),
    url(r'^spling/$', 'main.views.spling', name='spling'),
    url(r'^market/$', 'main.views.market', name='shop'),
    url(r'^market/([\w-]+)/$', 'main.views.market', name='shop_category'),
    
    # video pages - temporary link to shop
    url(r'^video/$', 'main.views.market', name='video'),
    url(r'^video/([\w-]+)/$', 'main.views.market', name='video_category'),

    url(r'^backend/$', 'backend.views.list', name='list'),
    url(r'^backend/bundle/(?P<id>.+)/$', 'backend.views.bundle', name='bundle'),
    url(r'^backend/add_to_spling/$', 'backend.views.add_to_spling', name='add_to_spling'),

    url(r'^([\w-]+)/([\w-]+)/([\w-]+)/([\w-]+)/$', 'main.views.board'),
    url(r'^([\w-]+)/([\w-]+)/([\w-]+)/$', 'main.views.board'),
    url(r'^([\w-]+)/([\w-]+)/$', 'main.views.board'),
    url(r'^([\w-]+)/$', 'main.views.board', name='board'),
)
