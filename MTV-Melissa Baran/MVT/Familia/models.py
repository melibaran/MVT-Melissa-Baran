from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    edad = models.IntegerField()
    cumpleanos = models.DateField()