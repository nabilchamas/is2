from django.conf.urls import patterns, url
from apps.burndownchart import views

urlpatterns = patterns('',

		# ej: prueba
		url(r'^chart/(?P<proyecto_id>\d+)/$', views.burndownchart_view, name="burndownchart"),
		url(r'^listar_proyectos_burndownchart/', views.listar_proyectos_burndownchart, name='listar_proyectos_burndownchart'),

	)
