from django.db import models

class Empleado(models.Model):

    dni = models.CharField(max_length=12)
    nombre = models.CharField(max_length=25)
    apellido1 = nombre = models.CharField(max_length=25)
    apellido2 = models.CharField(max_length=25)
    email = models.EmailField()
    telefono = models.IntegerField(max_length=14)

    class Meta:
        ordering = ["nombre"]




class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=25)
    nombre_contacto = models.CharField(max_length=25)
    apellido1_contacto = models.CharField(max_length=25)
    apellido2_contacto = models.CharField(max_length=25)
    telf_cliente = models.IntegerField(max_length=14)
    email_cliente = models.EmailField()

    class Meta:
        ordering = ["nombre_empresa"]




class Prioridad(models.Model):
    prioridad = models.CharField(max_length=15)

class Estado_Tarea(models.Model):
    estado_tarea = models.ManyToManyField() #PTE DE MIRAR!!!!
