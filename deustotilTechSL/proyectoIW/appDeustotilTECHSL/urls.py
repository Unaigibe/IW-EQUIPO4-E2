from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ProyectoListView.as_view(), name='home'),
    path('lista_proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos'),
    #path('lista_proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    #path('lista_proyectos/crear/', views.ProyectoNewView.as_view(), name='nuevo_proyecto'),
    #path('lista_proyectos/borrar', views.ProyectoDeleteView.as_view(), name='borrar_proyecto'),
    #path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),

#path('lista_clientes/<int:pk>/', views.ClientesDetailView.as_view(), name='proyecto'),

#path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),
#path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),
#path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),
#path('lista_proyectos/editar/', views.ProyectoEditView.as_view(), name='editar_proyecto'),

]