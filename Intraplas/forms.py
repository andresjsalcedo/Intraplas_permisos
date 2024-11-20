from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': None,
            
        }
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput,
        strip=False,
        help_text="",  # Personaliza o elimina el texto de ayuda aquí
    )
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text="",  # Personaliza o elimina el texto de ayuda aquí
    )

class LoginForm(AuthenticationForm):
    pass

