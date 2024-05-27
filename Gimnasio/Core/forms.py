from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=Usuario.USER_TYPE_CHOICES, required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'user_type', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
