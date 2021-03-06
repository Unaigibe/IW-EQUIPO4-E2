from datetime import date
from django.db import models


class Empleado(models.Model):
    dni = models.CharField(max_length=12)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True)
    nombre = models.CharField(max_length=25)
    apellido1 = models.CharField(max_length=25)
    apellido2 = models.CharField(max_length=25)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido1}'

PRIORIDADES = (
       ('Niguna','Niguna'),
       ('Baja', 'Baja'),
       ('Media','Media'),
       ('Alta','Alta'),
       ('Urgente','Urgente'),
)

ESTADO_TAREA = (
       ('Abierta','Abierta'),
       ('Asignada', 'Asignada'),
       ('En proceso','En proceso'),
       ('Cerrada','Cerrada'),
)


class Tarea(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField(default=date.today())
    fecha_fin = models.DateField(default=date.today())
    responsable = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)
    prioridad = models.CharField(max_length=25, choices=PRIORIDADES, default="Ninguna")
    estadoTarea = models.CharField(max_length=25, choices=ESTADO_TAREA, default="Asignada")
    nota_adicional = models.TextField(default='Rellena este campo con información adicional',max_length=750)

    def __str__(self):
        return f'{self.nombre}-> {self.descripcion}'


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=25)
    nombre_contacto = models.CharField(max_length=25)
    apellido1_contacto = models.CharField(max_length=25)
    apellido2_contacto = models.CharField(max_length=25)
    telf_cliente = models.IntegerField()
    email_cliente = models.EmailField()

    def __str__(self):
        return f'{self.nombre_empresa}'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField(default=date.today())
    fecha_fin = models.DateField(default=date.today())
    presupuesto = models.FloatField(default=0)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    tareas_a_realizar = models.ManyToManyField(Tarea)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f'{self.nombre} - Descripcion:  {self.descripcion}'
