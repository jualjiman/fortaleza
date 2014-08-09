from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortaleza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^contacto/$', 'administrador.views.contacto', name='contacto'),
    url(r'^imgProducto/$', 'administrador.views.imgProducto', name = 'imgProducto'),
    url(r'^catalogo-muebles/$', 'administrador.views.catalogo_muebles', name='catalogo_muebles'),
    url(r'^catalogo-muebles/(\d+)/$', 'administrador.views.catalogo_muebles_idc', name='catalogo_muebles-idc'),
    url(r'^catalogo-acabados/$', 'administrador.views.catalogo_acabados', name='catalogo_acabados'),
    url(r'^mueble/(\d+)/(\d+)/$', 'administrador.views.mueble', name='mueble'),
    url(r'^busqueda/$', 'administrador.views.busqueda', name='busqueda'),
)

urlpatterns += patterns('',url(r'^/webapps/fortalezac/fortaleza/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)
urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),)
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)
