from django.conf.urls import patterns, url
from usuario import views

urlpatterns = patterns('',

		# ej: usuario
		url(r'^$', views.menu_usuario, name='menu_usuario'),

		# ej: usuario/crear_usuario
		url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),

		# ej: usuario/modificar_usuario/3
		url(r'^modificar_usuario/(?P<usuario_id>\d+)/$', views.modificar_usuario, name='modificar_usuario'),

		# ej: usuario/ eliminar_usuario/4
		url(r'^eliminar_usuario/(?P<usuario_id>\d+)/$', views.eliminar_usuario, name='eliminar_usuario'),

		# ej: usuario/listar_usuario
		url(r'^listar_usuarios/$', views.listar_usuarios, name='listar_usuarios'),

	)



