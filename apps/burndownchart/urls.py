from django.conf.urls import patterns, url
from apps.burndownchart import views

urlpatterns = patterns('',

		# ej: prueba
		url(r'^$', views.burndownchart_view, name = "burndownchart"),

	)