from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class Usuario(AbstractBaseUser):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=255, null=True, blank=True)