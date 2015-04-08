from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm


class UsuarioModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_active']

        # password = forms.CharField(widget=forms.PasswordInput)
        # widgets = {
        #   'password':forms.PasswordInput(),
        # }
        
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Email',
            'is_active':'Activar usuario',
            'groups':'Perfiles',
        }

        help_texts = {
            'username':'(*) Requerido. 30 caracteres o menos. Letras, digitos y @/./+/-/_',
            # 'password':'(*)',
            'is_active':'',
            'groups':'',
        }

class CrearUsuarioModelForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': ("Los passwords son distintos."),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput,
        help_text=("(*)"))
    password2 = forms.CharField(label=("Password confirmacion"),
        widget=forms.PasswordInput,
        help_text=("(*)"))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 
            'first_name', 'last_name', 'email', 'groups', 'is_active']
        
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Email',
            'is_active':'Activar usuario',
            'groups':'Perfiles',
        }

        help_texts = {
            'username':'(*) Requerido. 30 caracteres o menos. Letras, digitos y @/./+/-/_',
            'password':'(*)',
            'is_active':'',
            'groups':'',
        }


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2



