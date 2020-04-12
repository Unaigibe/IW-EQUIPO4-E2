from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ProyectoListView.as_view(), name='home'),
    path('lista_proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos'),
    #path('lista_proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    #path('lista_proyectos/crear/', views.ProyectoNewView.as_view(), name='nuevo_proyecto'),
    #path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),
    #path('lista_proyectos/borrar', views.ProyectoDeleteView.as_view(), name='borrar_proyecto'),

    path('lista_tareas/', views.TareaListView.as_view(), name='lista_tareas'),
    path('lista_tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    path('lista_tareas/crear/', views.NuevaTarea.as_view(), name='nueva_tarea'),
    path('lista_tareas/escribir_nota/<int:pk>/', views.EscribirNota.as_view(), name='escribir_nota'),
    path('lista_tareas/modificar_tarea/<int:pk>/', views.ModificarTarea.as_view(), name='modificar_tarea'),
#    path('lista_tareas/borrar/<int:pk>/', views.BorrarTarea().as_view(), name='borrar_tarea'),

    path('lista_empleados/', views.EmpleadoListView.as_view(), name='lista_empleados'),
    path('lista_empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('lista_empleados/crear', views.NuevoEmpleado.as_view(), name='nuevo_empleado'),
    path('lista_modificar/modificar_empleado/<int:pk>/', views.ModificarEmpleado.as_view(), name='modificar_empleado'),

    path('lista_clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('lista_clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
    path('lista_clientes/crear', views.NuevoCliente.as_view(), name='nuevo_cliente'),
    path('lista_clientes/modificar_cliente/<int:pk>/', views.ModificarCliente.as_view(), name='modificar_cliente'),



]
