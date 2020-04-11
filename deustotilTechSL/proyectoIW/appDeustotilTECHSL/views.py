from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm


class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')
    template_name = "lista_proyectos.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Proyectos en Deustotil Tech SL'
        return context


#####ESPACIO PARA LAS VISTAS DE PROYECTOS
#
#
#

class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')
    template_name = "lista_tareas.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Tareas'
        return context


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de esta Tarea'
        return context
