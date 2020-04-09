from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ProyectoListView.as_view(), name='home'),
    path('lista_proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos')

]
