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
   #path('lista_tareas/editar/', views.ModificarTarea.as_view(), name='editar_tarea'),
   #path('lista_tareas/<int:pk>', views.deleteTarea().as_view(), name='borrar_tarea'),

    path('lista_empleados/', views.EmpleadoListView.as_view(), name='lista_empleados'),
    path('lista_empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('lista_empleados/crear', views.NuevoEmpleado.as_view(), name='nuevo_empleado'),



]
