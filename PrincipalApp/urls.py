from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Merlin'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'),
   path('Login/',  views.Login.as_view(), name='Login'),
   path('RegistroUsuario/', views.RegistroUsuario.as_view(), name='RegistroUsuario'),
   path('Logout/', views.LogoutUsuario.as_view(), name='Logout'),
   
   path('ListarProfesor/',views.ListProfesor.as_view(), name='ListarProfesor'),
   path('RegistrarProfesor/',views.CreatePorfesor.as_view(), name='RegistrarProfesor'),

   path('ListarMateria/',views.ListMateria.as_view(), name='ListarMateria'),
   path('RegistrarMateria/',views.CreateMateria.as_view(), name='RegistrarMateria'),
   path('UpdateMateria/<int:pk>/',views.UpdateMateria.as_view(), name='UpdateMateria'),

   path('RegistrarCurso/',views.CreateCurso.as_view(), name='RegistrarCurso'),
   path('ListarCurso/',views.ListCurso.as_view(), name='ListarCurso'),
   path('UpdateCurso/<int:pk>/',views.UpdateCurso.as_view(), name='UpdateCurso'),




   path('ListCursos/',views.ListCursos.as_view(), name='ListCursos'),
   path('DetalleCurso/<int:pk>/',views.DetCurso.as_view(), name='DetalleCurso'),

]


 