from django.db import models

class Prioridad(models.Model):
    prioridad = models.CharField(max_length=15)


class EstadoTarea(models.Model):
    estado_tarea = models.CharField(max_length=12)


class Empleado(models.Model):
    dni = models.CharField(max_length=12, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    apellido1 = nombre = models.CharField(max_length=25)
    apellido2 = models.CharField(max_length=25)
    email = models.EmailField()
    telefono = models.IntegerField(max_length=14)


class Tarea(models.Model):
    nombre = models.CharField(max_length=25, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.SET_NULL)
    prioridad = models.OneToOneField(Prioridad, on_delete=models.SET_NULL)
    estadoTarea = models.OneToOneField(EstadoTarea, on_delete=models.SET_NULL)
    nota_adicional = models.TextField(max_length=750)


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=25)
    nombre_contacto = models.CharField(max_length=25)
    apellido1_contacto = models.CharField(max_length=25)
    apellido2_contacto = models.CharField(max_length=25)
    telf_cliente = models.IntegerField(max_length=14)
    email_cliente = models.EmailField()


class Proyecto(models.Model):
    nombre = models.CharField(max_length=25, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL)
    tareas_a_realizar = models.ManyToManyField(Tarea)
    empleados = models.ManyToManyField(Empleado)

