from django.conf.urls import patterns, url
from apps.perfil import views

urlpatterns = patterns('',

		# ej: perfil
		url(r'^$', views.menu_perfil, name='menu_perfil'),

		# ej: perfil/crear_perfil
		url(r'^crear_perfil/$', views.crear_perfil, name='crear_perfil'),

		# ej: perfil/modificar_perfil/3
		url(r'^modificar_perfil/(?P<perfil_id>\d+)/$', views.modificar_perfil, name='modificar_perfil'),

		# ej: perfil/ eliminar_perfil/4
		url(r'^eliminar_perfil/(?P<perfil_id>\d+)/$', views.eliminar_perfil, name='eliminar_perfil'),

		# ej: perfil/listar_usuario
		url(r'^listar_perfiles/$', views.listar_perfiles, name='listar_perfiles'),



	)