from django.db import models

class TrabajadorReciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    antiguedad = models.PositiveIntegerField()

class TrabajadorAntiguo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    antiguedad = models.PositiveIntegerField()

class TrabajadorPrueba(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    antiguedad = models.PositiveIntegerField()

class Trabajador(models.Model):
    a= models.CharField(max_length=100)
    b= models.CharField(max_length=100)    
    c= models.CharField(max_length=100)