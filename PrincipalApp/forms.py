from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, Form, Select
from .models import *

 
class UsuarioForm(UserCreationForm):
    username = forms.CharField( max_length=140, required=False,widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control input-height'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control input-height'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control input-height'}))
    first_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control input-height'}))
    last_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control input-height'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control input-height'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = (
            'username', 
            'password'
        )
