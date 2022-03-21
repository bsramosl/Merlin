from pyexpat import model
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
  

class ProfesorForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'placeholder': 'Nombre','class': 'form-control input-height'}))
    area = forms.ModelChoiceField(queryset=Area.objects.all(),widget=forms.Select(attrs={'placeholder': 'Area','class': 'form-control input-height'}))
    materia = forms.ModelChoiceField(queryset=Materia.objects.all(),widget=forms.Select(attrs={'placeholder': 'Materia','class': 'form-control input-height'}))
    movil =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Numero de Movil','class': 'form-control input-height'}))
    generos= [
    ('M', 'Masculino'),
    ('F', 'Femenino'), 
    ] 
    genero = forms.ChoiceField(choices=generos, required=True, label="Seleccione su género",widget=forms.Select(attrs={'placeholder': 'Materia','class': 'form-control input-height'}))

    class Meta:
        model = Profesor
        fields = '__all__'


class MateriaForm(forms.ModelForm):
    nombre =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control input-height'}))
    
    class Meta:
        model = Materia
        fields = '__all__'

class CursoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre del Curso','class': 'form-control input-height'}))
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Detalle','class': 'form-control-textarea'}))
    fechainicio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seleccione Fecha','class': 'formDatePicker form-control flatpickr-input active'}))
    duracion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Duracion del Curso','class': 'form-control input-height'}))
    precio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Precio del Curso','class': 'form-control input-height'}))
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all(),widget=forms.Select(attrs={'placeholder': 'Profesor','class': 'form-control input-height'}))
    maxestudiante = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Estutiantes Maximo','class': 'form-control input-height'}))
    contacto = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Numero de Contacto','class': 'form-control input-height'}))
    imagen = forms.FileField(widget=forms.FileInput(attrs={'placeholder': 'Imagen','class': 'default'}))

    class Meta:
        model = Curso
        fields = '__all__'