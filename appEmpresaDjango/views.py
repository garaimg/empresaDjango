from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from appEmpresaDjango.forms import DepartamentoForm
from appEmpresaDjango.models import Empleado, Departamento, Habilidad


# 1. FBV para listar departamentos
def index_departamentos(request):
    departamentos = Departamento.objects.all()
    # output = ', '.join([d.nombre for d in departamentos])
    # return HttpResponse(output)
    return render(request, 'appEmpresaDjango/departamentos_index.html', {'departamentos': departamentos})


# 1. CBV para listar departamentos
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "appEmpresaDjango/departamentos_index.html"
    context_object_name = "departamentos"


# 2. FBV para ver el detalle de un departamento
def show_departamento(request, departamento_id):
    # departamento = Departamento.objects.get(id=departamento_id)
    departamento = get_object_or_404(Departamento, id=departamento_id)
    # output = f'Detalles del departamento: {departamento.id}, {departamento.nombre}, {departamento.telefono}'
    # return HttpResponse(output)
    return render(request, 'appEmpresaDjango/departamento_detail.html', {'departamento': departamento})


# 2. CBV para ver el detalle de un departamento
class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = "appEmpresaDjango/departamento_detail.html"
    context_object_name = "departamento"


# 3. FBV devuelve los empleados asociados a un departamento
def index_empleados(request, departamento_id):
    # departamento = Departamento.objects.get(pk=departamento_id)
    departamento = get_object_or_404(Departamento, id=departamento_id)
    # salida = ", ".join([e.nombre for e in departamento.empleado_set.all()])
    # return HttpResponse(salida)
    empleados = departamento.empleado_set.all()
    return render(request, 'appEmpresaDjango/empleados_index.html',
                  {'empleados': empleados, 'departamento': departamento})


# 3. CBV devuelve los empleados asociados a un departamento

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appEmpresaDjango/empleados_index.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        departamento = get_object_or_404(Departamento, id=self.kwargs['departamento_id'])
        return Empleado.objects.filter(departamento=departamento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamento = get_object_or_404(Departamento, pk=self.kwargs['departamento_id'])
        context['departamento'] = departamento
        context['usuario_conectado'] = "Jaime Urrutia"
        return context


# 4. FBV devuelve el detalle del empleado
def show_empleado(request, empleado_id):
    # empleado = Empleado.objects.get(pk=empleado_id)
    empleado = get_object_or_404(Empleado, id=empleado_id)
    # output = f'Detalles del empleado: {empleado.id}, {empleado.nombre}, {empleado.fecha_nacimiento}, {empleado.antiguedad},{str(empleado.departamento)}, Habilidades: {[h.nombre for h in empleado.habilidad.all()]}'
    # return HttpResponse(output)
    habilidades = empleado.habilidad.all()
    return render(request, 'appEmpresaDjango/empleado_detail.html', {'empleado': empleado, 'habilidades': habilidades})


# 4. CBV devuelve el detalle del empleado

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "appEmpresaDjango/empleado_detail.html"
    context_object_name = "empleado"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado = self.get_object()
        context['habilidades'] = empleado.habilidad.all()
        return context


def show_habilidad(request, habilidad_id):
    # habilidad = Habilidad.objects.get(pk=habilidad_id)
    habilidad = get_object_or_404(Habilidad, id=habilidad_id)
    output = (f'Detalles de la habilidad: {habilidad.id}, {habilidad.nombre},'
              f' Empleados :{[e.nombre for e in habilidad.empleado_set.all()]}')
    return HttpResponse(output)


class DepartamentoCreateView(View):

    def get(self, request):
        formulario = DepartamentoForm()
        context = {'formulario': formulario}
        return render(request, 'appEmpresaDjango/departamento_create.html', context)

    def post(self, request):
        formulario = DepartamentoForm(data=request.POST)
        if formulario.is_valid():
            # Opción A:
            # departamento = Departamento()
            # departamento.nombre = formulario.cleaned_data['nombre']
            # departamento.telefono = formulario.cleaned_data['telefono']
            # departamento.save()
            # Opción B:
            formulario.save()
            return redirect('index')

        return render(request, 'appEmpresaDjango/departamento_create.html', {'formulario': formulario})
