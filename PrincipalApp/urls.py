from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Merlin'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'),
   path('ListCategoria/',views.ListCategoria.as_view(), name='ListCategoria'),
   path('RegistrarCategoria/',views.CreateCategoria.as_view(), name='RegistrarCategoria'),
   path('EditarCategoria/<int:pk>',views.UpdateCategoria.as_view(), name='EditarCategoria'),

    path('RegistrarPregunta/',views.CreatePregunta.as_view(), name='RegistrarPregunta'),
   path('ListPregunta/',views.ListPregunta.as_view(), name='ListPregunta'),
    
]