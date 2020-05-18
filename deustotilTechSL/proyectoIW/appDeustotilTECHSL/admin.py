from django.contrib import admin
from .models import Empleado, Cliente, Tarea, Proyecto

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Tarea)
admin.site.register(Proyecto)
