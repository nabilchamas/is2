# django imports
from django import forms
from django.contrib.admin.forms import forms as adminforms

# third party imports
from db_file_storage.form_widgets import DBClearableFileInput, \
    DBAdminClearableFileInput

# project imports
from music.models import CD, SoundDevice


class CDForm(forms.ModelForm):
    class Meta(object):
        model = CD
        exclude = []
        widgets = {
            'disc': DBClearableFileInput,
            'cover': DBClearableFileInput,
        }


class CDAdminForm(adminforms.ModelForm):
    class Meta(object):
        model = CD
        exclude = []
        widgets = {
            'disc': DBAdminClearableFileInput,
            'cover': DBAdminClearableFileInput,
        }


class SoundDeviceForm(forms.ModelForm):
    class Meta(object):
        model = SoundDevice
        exclude = []
