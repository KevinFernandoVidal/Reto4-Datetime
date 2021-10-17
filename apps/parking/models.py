from django.db import models
from apps.usuario.models import Persona

# Create your models here.

class TipoVehiculo(models.Model):
    Vehiculo = models.CharField(max_length=45)
    def __str__(self):
        return self.Vehiculo

class Vehiculo(models.Model):
    marca   = models.CharField(max_length=100)
    modelo  = models.CharField(max_length=100)
    tipo    = models.ForeignKey(TipoVehiculo ,on_delete=models.CASCADE)
    placa   = models.CharField(max_length=50)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca +" "+ self.modelo

class Servicio(models.Model):
    nombre      = models.CharField(max_length=50)
    valor       = models.PositiveIntegerField()
    clase =(('Horas', 'Horas'),('Mensual', 'Mensual'),('Nocturno', 'Nocturno'),)
    tipos       = models.CharField(choices=clase, max_length=10)
    estado      = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    fecha_creacion  = models.DateTimeField(auto_now_add=True)
    total           = models.PositiveIntegerField(null=True, blank=True, default=0)
    estado          = models.BooleanField(default=False)

class Factura_servicio(models.Model):
    servicio        = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    factura         = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad        = models.IntegerField()
    vehiculo        = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    hora_inicio     = models.DateTimeField()
    hora_fin        = models.DateTimeField()
    subtotal        = models.PositiveIntegerField()
