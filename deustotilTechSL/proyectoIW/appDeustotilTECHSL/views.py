from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


from .models import Proyecto, Tarea, Empleado, Cliente
from .forms import ProyectoForm, TareaForm, EmpleadoForm, ClienteForm, \
    UpdateNotaTareaForm, ModificarProyectoForm, ModificarTareaForm


def home(request):
    numProyectos = Proyecto.objects.all().count()
    numClientes = Cliente.objects.all().count()
    numEmpleados = Empleado.objects.all().count()
    context = {'numProyectos': numProyectos, 'numClientes': numClientes, 'numEmpleados': numEmpleados,
               'titulo_pagina': 'Nuestra empresa'}
    return render(request, 'home.html', context)


# ESPACIO PARA LAS VISTAS DE PROYECTOS

class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')
    template_name = "lista_proyectos.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Proyectos'
        return context


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de este Proyecto'
        return context


class NuevoProyecto(View):

    def get(self, request, *args, **kwargs):
        form = ProyectoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear un proyecto'
        }
        return render(request, 'nuevo_proyecto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
        return render(request, 'nuevo_proyecto.html', {'form': form})


class ModificarProyecto(UpdateView):
    model = Proyecto
    form_class = ModificarProyectoForm
    template_name = 'modificar_proyecto.html'
    success_url = '/index/lista_proyectos'


class EliminarProyecto(DeleteView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'eliminar_proyecto.html'
    success_url = '/index/lista_proyectos'


# ESPACIO PARA LAS VISTAS DE TAREAS
#

"""class TareaProyectoListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')
    template_name = "tareas_proyecto.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Tareas en este proyecto'
        return context
"""


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


class ModificarTarea(UpdateView):
    model = Tarea
    form_class = ModificarTareaForm
    template_name = 'modificar_tarea.html'
    success_url = '/index/lista_tareas'


class EscribirNota(UpdateView):
    model = Tarea
    form_class = UpdateNotaTareaForm
    template_name = 'escribir_nota.html'
    success_url = '/index/lista_tareas'


class EliminarTarea(DeleteView):
    model = Tarea
    form_class = TareaForm
    template_name = 'eliminar_tarea.html'
    success_url = '/index/lista_tareas'


# ESPACIO PARA LAS VISTAS DE EMPLEADO


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
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        return render(request, 'nuevo_empleado.html', {'form': form})


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Ficha de Empleado'
        return context


class ModificarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'modificar_empleado.html'
    success_url = '/index/lista_empleados/'


class EliminarEmpleado(DeleteView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'eliminar_empleado.html'
    success_url = '/index/lista_empleados/'


#####ESPACIO PARA LAS VISTAS DE CLIENTE
#


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


class ModificarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'modificar_cliente.html'
    success_url = '/index/lista_clientes'


class EliminarCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'eliminar_cliente.html'
    success_url = '/index/lista_clientes/'
