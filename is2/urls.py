from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'is2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^proyecto/', include('proyecto.urls', namespace='proyecto')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^inicio/', include('inicio.urls', namespace='inicio')),
    url(r'^perfil/', include('perfil.urls', namespace='perfil')),
)
