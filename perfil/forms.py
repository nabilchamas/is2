from django.contrib.auth.models import Group
from django import forms


class PerfilModelForm(forms.ModelForm):

    class Meta:
        model = Group
        # fields = ['name', 'permissions']
        fields = '__all__'

        help_texts = {
            'permissions':'',
        }


