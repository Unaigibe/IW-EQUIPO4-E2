from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView

from .models import Proyecto, Tarea, Empleado, Cliente


@method_decorator(csrf_exempt, name='dispatch')


def home(request):
    numProyectos = Proyecto.objects.all().count()
    numClientes = Cliente.objects.all().count()
    numEmpleados = Empleado.objects.all().count()
    context = {'numProyectos': numProyectos, 'numClientes': numClientes, 'numEmpleados': numEmpleados,
               'titulo_pagina': 'Nuestra empresa'}
    return render(request, 'home.html', context)

class APIListaClientesView(View):
    def get(self, request):
        listaClientes = Cliente.objects.all()
        return JsonResponse(list(listaClientes.values()), safe=False)

    def post(self, request):
        cliente = Cliente()
        cliente.nombre_empresa = request.POST["nombre_empresa"]
        cliente.nombre_contacto = request.POST["nombre_contacto"]
        cliente.apellido1_contacto = request.POST["apellido1_contacto"]
        cliente.apellido2_contacto = request.POST["apellido2_contacto"]
        cliente.telf_cliente = request.POST["telf_cliente"]
        cliente.email_cliente = request.POST["email_cliente"]
        cliente.save()
        return JsonResponse(model_to_dict(cliente))


class ListaClientesView(TemplateView):
    template_name = 'lista_clientes.html'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de este Cliente'
        return context



@method_decorator(csrf_exempt, name='dispatch')
class APIListaEmpleadosView(View):
    def get(self, request):
        listaEmpleados = Empleado.objects.all()
        return JsonResponse(list(listaEmpleados.values()), safe=False)


class ListaEmpleadosView(TemplateView):
    template_name = 'lista_empleados.html'


class APIListaProyectosView(View):
    def get(self, request):
        listaProyectos = Proyecto.objects.all()
        return JsonResponse(list(listaProyectos.values()), safe=False)


class ListaProyectosView(TemplateView):
    template_name = 'lista_proyectos.html'


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de este Proyecto'
        return context


class APIListaTareasView(View):
    def get(self, request):
        listaTareas = Tarea.objects.all()
        return JsonResponse(list(listaTareas.values()), safe=False)


class ListaTareasView(TemplateView):
    template_name = 'lista_tareas.html'


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de esta Tarea'
        return context


"""
    def post(self, request):
        empleado = Empleado()
        empleado.dni = request.POST["dni"]
        empleado.foto_perfil = request.POST["foto_perfil"]
        empleado.nombre = request.POST["nombre"]
        empleado.apellido1 = request.POST["apellido1"]
        empleado.apellido2 = request.POST["apellido2"]
        empleado.email = request.POST["email"]
        empleado.telefono = request.POST["telefono"]
        empleado.save()
        return JsonResponse(model_to_dict(empleado))
"""

class EmpleadoDetailView(View):
    def get(self, request,pk):
        empleado = Empleado.objects.get(pk=pk)
        urlFotoEmpleado = empleado.foto_perfil.url
        libEmpleado = model_to_dict(empleado)
        libEmpleado['foto_perfil'] = urlFotoEmpleado
        return JsonResponse(libEmpleado)


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Ficha de Empleado'
        return context




"""
# VISTA HOME
#EN esta vista se muestran 3 variables de la BBDD. Dichas variables aparecerán en la vista home mostrando cuantos proyectos, clientes y empleados existen.



# VISTAS PARA PROYECTOS
# Permite listar todos los proyectos contenidos en la BBDD
class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')
    template_name = "lista_proyectos.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Proyectos'
        return context


# Permite visualizar todos los campos de un proyecto



# Permite crear un proyecto nuevo
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


# Permite modificar un proyecto existente
class ModificarProyecto(UpdateView):
    model = Proyecto
    form_class = ModificarProyectoForm
    template_name = 'modificar_proyecto.html'
    success_url = '/index/lista_proyectos'


# Permite eliminar un proyecto existente
class EliminarProyecto(DeleteView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'eliminar_proyecto.html'
    success_url = '/index/lista_proyectos'


# VISTAS PARA TAREAS
# Permite listar todas las tareas contenidas en la BBDD
class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')
    template_name = "lista_tareas.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Tareas'
        return context


# Permite visualizar todos los campos de una tarea



# Permite crear una tarea nueva
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


# Permite modificar una tarea existente
class ModificarTarea(UpdateView):
    model = Tarea
    form_class = ModificarTareaForm
    template_name = 'modificar_tarea.html'
    success_url = '/index/lista_tareas'


# Permite escribir una nota en una tarea existente
class EscribirNota(UpdateView):
    model = Tarea
    form_class = UpdateNotaTareaForm
    template_name = 'escribir_nota.html'
    success_url = '/index/lista_tareas'


# Permite eliminar una tarea existente
class EliminarTarea(DeleteView):
    model = Tarea
    form_class = TareaForm
    template_name = 'eliminar_tarea.html'
    success_url = '/index/lista_tareas'


# VISTAS PARA EMPLEADO
# Permite listar todos los empleados contenidos en la BBDD
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')
    template_name = "lista_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Empleados'
        return context


# Permite crear un empleado nuevo
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





# Permite modificar un empleado existente
class ModificarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'modificar_empleado.html'
    success_url = '/index/lista_empleados/'


# Permite eliminar un empleado existente
class EliminarEmpleado(DeleteView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'eliminar_empleado.html'
    success_url = '/index/lista_empleados/'


# VISTAS PARA CLIENTE
# Permite listar todos los clientes contenidos en la BBDD
class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre_empresa')
    template_name = "lista_clientes.html"

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Clientes'
        return context


# Permite crear un cliente nuevo
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


# Permite visualizar todos los campos de un cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle de este Cliente'
        return context


# Permite modificar un cliente existente
class ModificarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'modificar_cliente.html'
    success_url = '/index/lista_clientes'


# Permite eliminar un cliente existente
class EliminarCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'eliminar_cliente.html'
    success_url = '/index/lista_clientes/'

"""
