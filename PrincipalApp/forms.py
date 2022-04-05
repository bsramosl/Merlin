from re import A
from .models import *
from django import forms

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    
    
    class Meta:
        model = Categoria
        fields = '__all__'


class PreguntaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-textarea'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),widget=forms.Select(attrs={'class': 'form-select input-height'}))
    a = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    b = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    c = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    d = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Pregunta
        fields = '__all__'

