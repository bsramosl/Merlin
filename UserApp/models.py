from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    LOAN_ROL = (
        ('S', 'Admin'),
        ('P', 'Profesor'), 
        ('U', 'Usuario'), 

    )
    rol = models.CharField(max_length=1, choices= LOAN_ROL, blank=True,null=True, default='U', help_text='Rol')