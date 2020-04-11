from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ProyectoListView.as_view(), name='home'),
    path('lista_proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos'),
    #path('lista_proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    #path('lista_proyectos/crear/', views.ProyectoNewView.as_view(), name='nuevo_proyecto'),
    #path('lista_proyectos/borrar', views.ProyectoDeleteView.as_view(), name='borrar_proyecto'),
    #path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),
    # path('lista_tareas/', views.TareaListView.as_view(), name='lista_tareas'),
    # path('lista_tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    # path('lista_tareas/crear/', views.TareaNewView.as_view(), name='nueva_tarea'),
]
