from apps.flujo.models import Flujo, Actividad
from django import forms

class FlujoModelForm(forms.ModelForm):
	class Meta:
		model = Flujo

class ActividadModelForm(forms.ModelForm):
	class Meta:
		model = Actividad




