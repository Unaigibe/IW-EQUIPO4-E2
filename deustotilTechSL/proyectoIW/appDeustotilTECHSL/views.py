from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Proyecto, Tarea, Empleado, Cliente
from .forms import ProyectoForm, TareaForm, EmpleadoForm, ClienteForm


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


class NuevaTarea(View):
    def get(self, request, *args, **kwargs):
        form = TareaForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear una tarea'
        }
        return render(request, 'nueva_tarea.html', context)

    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
        return render(request, 'nueva_tarea.html', {'form': form})


class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')
    template_name = "lista_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Empleados'
        return context


class NuevoEmpleado(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear un empleado'
        }
        return render(request, 'nuevo_empleado.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        return render(request, 'nuevo_empleado.html', {'form': form})


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de este Empleado'
        return context


class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre_empresa')
    template_name = "lista_clientes.html"

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Clientes'
        return context


class NuevoCliente(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear un cliente'
        }
        return render(request, 'nuevo_cliente.html', context)

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
        return render(request, 'nuevo_cliente.html', {'form': form})


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de este Cliente'
        return context
