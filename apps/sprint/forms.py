from apps.sprint.models import Sprint
from django import forms

class SprintModelForm(forms.ModelForm):
	class Meta:
		model = Sprint
		fields = '__all__'



