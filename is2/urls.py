from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'is2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^proyecto/', include('apps.proyecto.urls', namespace='proyecto')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^inicio/', include('apps.inicio.urls', namespace='inicio')),
    url(r'^perfil/', include('apps.perfil.urls', namespace='perfil')),
    url(r'^flujo/', include('apps.flujo.urls', namespace='flujo')),
    url(r'^userstory/', include('apps.userstory.urls', namespace='userstory')),
    url(r'^sprint/', include('apps.sprint.urls', namespace='sprint')),
    url(r'^burndownchart/', include('apps.burndownchart.urls', namespace='burndownchart')),
)
