from apps.sprint.models import Sprint
from django import forms

class SprintModelForm(forms.ModelForm):
	class Meta:
		model = Sprint
		fields = '__all__'

		widgets = {
			'fecha_inicio': forms.DateInput(attrs={'class':'datepicker'}),
			'fecha_fin': forms.DateInput(attrs={'class':'datepicker'}),

		}




