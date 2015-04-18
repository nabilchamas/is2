from apps.userstory.models import UserStory
from django import forms

class UserStoryModelForm(forms.ModelForm):
	class Meta:
		model = UserStory
		fields = '__all__'




