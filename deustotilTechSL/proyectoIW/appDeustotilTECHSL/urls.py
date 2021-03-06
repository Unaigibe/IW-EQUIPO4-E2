from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('api_empleados/', views.APIListaEmpleadosView.as_view(), name='api_lista_empleados'),
    path('lista_empleados/', views.ListaEmpleadosView.as_view(), name='lista_empleados'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),


    path('api_proyectos/', views.APIListaProyectosView.as_view(), name='api_lista_proyectos'),
    path('lista_proyectos/', views.ListaProyectosView.as_view(), name='lista_proyectos'),
    path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),


    path('api_clientes/', views.APIListaClientesView.as_view(), name='api_lista_clientes'),
    path('lista_clientes/', views.ListaClientesView.as_view(), name='lista_clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),

    path('api_tareas/', views.APIListaTareasView.as_view(), name='api_lista_tareas'),
    path('lista_tareas/', views.ListaTareasView.as_view(), name='lista_tareas'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),

    ]
"""
    
   
    
    path('clientes/', views.ListaClientesView.as_view(), name='lista_clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
    path('lista_proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos'),
    path('lista_proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('lista_proyectos/crear/', views.NuevoProyecto.as_view(), name='nuevo_proyecto'),
    path('lista_proyectos/editar/', views.TareaListView.as_view(), name='lista_tareas'),
    path('lista_tareas/modificar_proyecto/<pk>/', views.ModificarProyecto.as_view(), name='modificar_proyecto'),
    path('lista_tareas/eliminar_proyecto/<pk>/', views.EliminarProyecto.as_view(), name='eliminar_proyecto'),

    path('lista_tareas/', views.TareaListView.as_view(), name='lista_tareas'),
    path('lista_tareas/crear/', views.NuevaTarea.as_view(), name='nueva_tarea'),
    path('lista_tareas/escribir_nota/<pk>/', views.EscribirNota.as_view(), name='escribir_nota'),
    path('lista_tareas/modificar_tarea/<pk>/', views.ModificarTarea.as_view(), name='modificar_tarea'),
    path('lista_tareas/eliminar_tarea/<pk>/', views.EliminarTarea.as_view(), name='eliminar_tarea'),

    path('lista_empleados/', views.EmpleadoListView.as_view(), name='lista_empleados'),
    path('lista_empleados/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('lista_empleados/crear', views.NuevoEmpleado.as_view(), name='nuevo_empleado'),
    path('lista_empleados/modificar_empleado/<pk>/', views.ModificarEmpleado.as_view(), name='modificar_empleado'),
    path('lista_empleados/eliminar_empleado/<pk>/', views.EliminarEmpleado.as_view(), name='eliminar_empleado'),

    path('lista_clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('lista_clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
    path('lista_clientes/crear', views.NuevoCliente.as_view(), name='nuevo_cliente'),
    path('lista_clientes/modificar_cliente/<pk>/', views.ModificarCliente.as_view(), name='modificar_cliente'),
    path('lista_clientes/eliminar_cliente/<pk>/', views.EliminarCliente.as_view(), name='eliminar_cliente'),

"""
