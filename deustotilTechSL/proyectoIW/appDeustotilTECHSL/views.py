from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, ListView

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


class ListaClientesView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'
    context_object_name = 'lista_clientes'

    def get_context_data(self, **kwargs):
        context = super(ListaClientesView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Clientes'
        return context

    def post(self, request):
        cliente = Cliente()
        cliente.nombre_empresa = request.POST['nombre_empresa']
        cliente.nombre_contacto = request.POST['nombre_contacto']
        cliente.apellido1_contacto = request.POST['apellido1_contacto']
        cliente.apellido2_contacto = request.POST['apellido2_contacto']
        cliente.telf_cliente = request.POST['telf_cliente']
        cliente.email_cliente = request.POST['email_cliente']
        cliente.save()
        return JsonResponse(model_to_dict(cliente))


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
