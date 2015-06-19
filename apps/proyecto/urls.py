from django.conf.urls import patterns, url
from apps.proyecto import views

urlpatterns = patterns('',

		# ej: proyecto/
		url(r'^$', views.menu_proyecto, name='menu_proyecto'),

		# ej: proyecto/crear_proyecto
		url(r'^crear_proyecto/$', views.crear_proyecto, name='crear_proyecto'),

		# ej: proyecto/modificar_proyecto/3
		url(r'^modificar_proyecto/(?P<proyecto_id>\d+)/$', views.modificar_proyecto, name='modificar_proyecto'),

		# ej: proyecto/eliminar_proyecto/4
		url(r'^eliminar_proyecto/(?P<proyecto_id>\d+)/$', views.eliminar_proyecto, name='eliminar_proyecto'),

		# ej: proyecto/listar_proyectos
		url(r'^listar_proyectos/', views.listar_proyectos, name='listar_proyectos'),

		# ej: proyecto/informe_proyecto/2
		url(r'^informe_proyecto/(?P<proyecto_id>\d+)/$', views.informe_proyecto, name='informe_proyecto'),

	)













