from django.conf.urls import patterns, url
from apps.userstory import views

urlpatterns = patterns('',

		# ej: userstory/
		url(r'^$', views.menu_userstory, name='menu_userstory'),

		# ej: userstory/crear_userstory
		url(r'^crear_userstory/$', views.crear_userstory, name='crear_userstory'),

		# ej: userstory/modificar_userstory/3
		url(r'^modificar_userstory/(?P<userstory_id>\d+)/$', views.modificar_userstory, name='modificar_userstory'),

		# ej: userstory/eliminar_userstory/4
		url(r'^eliminar_userstory/(?P<userstory_id>\d+)/$', views.eliminar_userstory, name='eliminar_userstory'),

		# ej: userstory/listar_userstories
		url(r'^listar_userstories/', views.listar_userstories, name='listar_userstories'),

		# ej: userstory/modificar_en_flujo/3
		url(r'^modificar_en_flujo/(?P<userstory_id>\d+)/$', views.modificar_en_flujo, name='modificar_en_flujo'),

	)