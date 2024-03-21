from django.http import HttpResponse
from django.shortcuts import render

from appEmpresaDjango.models import Empleado


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def index2(request):
    empleados = Empleado.objects.all()
    salida = ", ".join([e.nombre for e in empleados])
    return HttpResponse(salida)
