from django.conf.urls import patterns, url
from flujo import views

urlpatterns = patterns('',

		# ej: flujo/
		url(r'^$', views.menu_flujo, name='menu_flujo'),

		# ej: flujo/crear_flujo
		url(r'^crear_flujo/$', views.crear_flujo, name='crear_flujo'),

		# ej: flujo/modificar_flujo/3
		url(r'^modificar_flujo/(?P<flujo_id>\d+)/$', views.modificar_flujo, name='modificar_flujo'),

		# ej: flujo/eliminar_flujo/4
		url(r'^eliminar_flujo/(?P<flujo_id>\d+)/$', views.eliminar_flujo, name='eliminar_flujo'),

		# ej: flujo/listar_flujos
		url(r'^listar_flujos/', views.listar_flujos, name='listar_flujos'),

		# ej: flujo/desplegar_flujo/3
		url(r'^desplegar_flujo/(?P<flujo_id>\d+)/$', views.desplegar_flujo, name='desplegar_flujo'),


		# Actividades



		# ej: flujo/menu_actividad
		url(r'^menu_actividad/$', views.menu_actividad, name='menu_actividad'),


		# ej: flujo/crear_actividad
		url(r'^crear_actividad/$', views.crear_actividad, name='crear_actividad'),

		# ej: flujo/modificar_actividad/3
		url(r'^modificar_actividad/(?P<actividad_id>\d+)/$', views.modificar_actividad, name='modificar_actividad'),

		# ej: flujo/eliminar_actividado/4
		url(r'^eliminar_actividad/(?P<actividad_id>\d+)/$', views.eliminar_actividad, name='eliminar_actividad'),

		# ej: flujo/listar_actividads
		url(r'^listar_actividades/', views.listar_actividades, name='listar_actividades'),


	)