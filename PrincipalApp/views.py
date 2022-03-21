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



class CreatePorfesor(LoginRequiredMixin,CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'admin/RegistrarProfesor.html'
    success_url = reverse_lazy('Merlin:ListarProfesor')

class ListProfesor(LoginRequiredMixin,ListView):
    model = Profesor
    template_name = 'admin/ListarProfesor.html'




class CreateMateria(LoginRequiredMixin,CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'admin/RegistrarMateria.html'
    success_url = reverse_lazy('Merlin:ListarMateria')

class ListMateria(LoginRequiredMixin,ListView):
    model = Materia
    template_name = 'admin/ListarMateria.html'

class UpdateMateria(UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'admin/ActualizarMateria.html'
    success_url = reverse_lazy('Merlin:ListarMateria')


class CreateCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'admin/RegistrarCurso.html'
    success_url = reverse_lazy('Merlin:ListarCurso')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

class ListCurso(ListView):
    model = Curso
    template_name ='admin/ListarCurso.html'


class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name ='admin/ActualizarCurso.html'
    success_url = reverse_lazy('Merlin:ListarCurso')








class ListCursos(ListView):
    model = Curso
    template_name = 'ListaCurso.html'

class DetCurso(DetailView):
    model = Curso
    template_name = 'DetalleCurso.html'