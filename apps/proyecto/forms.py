from apps.proyecto.models import Proyecto
from django import forms

class ProyectoModelForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ('nombre', 'codigo', 'descripcion', 'cliente')