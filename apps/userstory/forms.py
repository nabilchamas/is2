from apps.userstory.models import UserStory
from django import forms
from db_file_storage.form_widgets import DBClearableFileInput

class UserStoryModelForm(forms.ModelForm):
	class Meta:
		model = UserStory
		fields = '__all__'
		widgets = {
            'adjunto': DBClearableFileInput
        }




