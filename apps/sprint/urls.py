from django.conf.urls import patterns, url
from apps.sprint import views

urlpatterns = patterns('',

		# ej: sprint/
		url(r'^$', views.menu_sprint, name='menu_sprint'),

		# ej: sprint/crear_sprint
		url(r'^crear_sprint/$', views.crear_sprint, name='crear_sprint'),

		# ej: sprint/modificar_sprint/3
		url(r'^modificar_sprint/(?P<sprint_id>\d+)/$', views.modificar_sprint, name='modificar_sprint'),

		# ej: sprint/eliminar_sprint/4
		url(r'^eliminar_sprint/(?P<sprint_id>\d+)/$', views.eliminar_sprint, name='eliminar_sprint'),
		# ej: sprint/listar_sprints
		url(r'^listar_sprints/', views.listar_sprints, name='listar_sprints'),


	)