from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from django.views.generic.edit import FormView
from .forms import *
from .models import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin,TemplateView):
    login_url = '/Login/'
    template_name = 'Index.html'


class Login(FormView):
    template_name = 'Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Merlin:Index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs) 

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class LogoutUsuario(RedirectView):
    pattern_name = 'Merlin:Login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class RegistroUsuario(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'RegistroUsuario.html'
    success_url = reverse_lazy('Merlin:Login')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response


class ListProfesor(ListView):
    model = Profesor
    template_name = 'admin/ListarProfesor.html'