from django.contrib import admin
from .models import Empleado, EstadoTarea, Cliente, Tarea, Prioridad, Proyecto

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Tarea)
admin.site.register(EstadoTarea)
admin.site.register(Prioridad)
admin.site.register(Proyecto)
