from apps.proyecto.models import Proyecto
from django import forms

class ProyectoModelForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields ='__all__'

		widgets = {
			'fecha_inicio': forms.DateInput(attrs={'class':'datepicker'}),
			'fecha_fin': forms.DateInput(attrs={'class':'datepicker'}),
		}


