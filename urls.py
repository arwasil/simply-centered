from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'spling/$', 'main.views.spling', name='spling'),
    url(r'shop/$', 'main.views.shop', name='shop'),

    url(r'^backend/$', 'backend.views.list', name='list'),
    url(r'^backend/bundle/(?P<id>.+)/$', 'backend.views.bundle', name='bundle'),

    url(r'^([\w-]+)/([\w-]+)/([\w-]+)$', 'main.views.board'),
    url(r'^([\w-]+)/([\w-]+)$', 'main.views.board'),
    url(r'^([\w-]+)$', 'main.views.board', name='board'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
