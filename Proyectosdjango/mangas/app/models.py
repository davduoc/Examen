from django.db import models

# Create your models here.

class Manga(models.Model):
    nombre = models.CharField(max_length=50)
    tomo = models.FloatField()
    editorial = models.CharField(max_length=30)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50, null=True)

    def str(self):
        return self.nombre