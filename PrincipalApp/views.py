from pyexpat import model
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from .models import *
from .forms import *

# Create your views here.


class Index(TemplateView):
    template_name = 'principal/Index.html'
 


class CreateCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'dashboard/registrarcategoria.html'
    success_url = reverse_lazy('Merlin:ListCategoria')


class ListCategoria(ListView):
    model = Categoria
    template_name = 'dashboard/listarcategoria.html'

class UpdateCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'dashboard/editarcategoria.html'
    success_url = reverse_lazy('Merlin:ListCategoria')

class CreatePregunta(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'dashboard/registrarpregunta.html'
    success_url = reverse_lazy('Merlin:ListPregunta')


class ListPregunta(ListView):
    model = Pregunta
    template_name = 'dashboard/listarpregunta.html'