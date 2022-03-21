from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    nombre = nombre = models.CharField(max_length=20,blank=False, null=False)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering =['nombre']
    
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=20,blank=False, null=False)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering =['nombre']
    
    def __str__(self):
        return self.nombre
    

class Profesor(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,blank=False, null=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE,blank=False, null=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE,blank=False, null=False)
    movil = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    LOAN_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'), 
    )
    genero = models.CharField(max_length=1, choices= LOAN_GENERO, blank=True, default='M', help_text='Genero')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering =['usuario']
    
    def __str__(self):
        return self.usuario.first_name + ' ' + self.usuario.last_name

    
class Curso(models.Model):
    nombre = models.CharField(max_length=30,blank=False, null=False)
    detalle = models.CharField(max_length=30,blank=False, null=False)
    fechainicio = models.DateField(blank=False, null=False)
    duracion = models.IntegerField(blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,blank=False, null=False)
    maxestudiante = models.IntegerField(blank=False, null=False)
    contacto = models.IntegerField(blank=False, null=False)
    imagen = models.ImageField('Imagen',upload_to='img/',blank=True, null=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



