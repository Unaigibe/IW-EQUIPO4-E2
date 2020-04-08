from django.db import models


class Prioridad(models.Model):
    prioridad = models.CharField(max_length=15)

    def __str__(self):
        return self.prioridad


class EstadoTarea(models.Model):
    estado_tarea = models.CharField(max_length=12)

    def __str__(self):
        return self.estado_tarea


class Empleado(models.Model):
    dni = models.CharField(max_length=12)
    nombre = models.CharField(max_length=25)
    apellido1 = models.CharField(max_length=25)
    apellido2 = models.CharField(max_length=25)
    email = models.EmailField()
    telefono = models.IntegerField()


class Tarea(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.OneToOneField(Prioridad, on_delete=models.CASCADE)
    estadoTarea = models.OneToOneField(EstadoTarea, on_delete=models.CASCADE)
    nota_adicional = models.TextField(max_length=750)


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=25)
    nombre_contacto = models.CharField(max_length=25)
    apellido1_contacto = models.CharField(max_length=25)
    apellido2_contacto = models.CharField(max_length=25)
    telf_cliente = models.IntegerField()
    email_cliente = models.EmailField()


class Proyecto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.FloatField()
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    tareas_a_realizar = models.ManyToManyField(Tarea)
    empleados = models.ManyToManyField(Empleado)

