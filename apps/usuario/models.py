from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    cedula   = models.IntegerField(unique=True)
    nombre   = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    id_user  = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 