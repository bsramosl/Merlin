from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Merlin'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'),
   path('Login/',  views.Login.as_view(), name='Login'),
   path('RegistroUsuario/', views.RegistroUsuario.as_view(), name='RegistroUsuario'),
   path('Logout/', views.LogoutUsuario.as_view(), name='Logout'),


   path('ListarUsuario/',views.ListUsuario.as_view(), name='ListarUsuario'),
    path('RegistrarUsuario/',views.CreateUsuario.as_view(), name='RegistrarUsuario'),
     path('UpdateUsuario/<int:pk>/',views.UpdateUsuario.as_view(), name='UpdateUsuario'),

   
   path('ListarPersona/',views.ListPersona.as_view(), name='ListarPersona'),
   path('RegistrarPersona/',views.CreatePersona.as_view(), name='RegistrarPersona'),
   path('UpdatePersona/<int:pk>/',views.UpdatePersona.as_view(), name='UpdatePersona'),
 
 
   path('RegistrarCurso/',views.CreateCurso.as_view(), name='RegistrarCurso'),
   path('ListarCurso/',views.ListCurso.as_view(), name='ListarCurso'),
   path('UpdateCurso/<int:pk>/',views.UpdateCurso.as_view(), name='UpdateCurso'),




   path('ListCursos/',views.ListCursos.as_view(), name='ListCursos'),
   path('DetalleCurso/<int:pk>/',views.DetCurso.as_view(), name='DetalleCurso'),

]


 