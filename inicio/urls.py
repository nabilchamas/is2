from django.conf.urls import patterns, url
from inicio import views

urlpatterns = patterns('',

		# ej: inicio/
		url(r'^$', views.autenticar, name='autenticar'),

		# ej: inicio/menu
		url(r'^menu/$', views.menu, name='menu'),

		url(r'^salir/$', views.salir, name='salir'),

	)



