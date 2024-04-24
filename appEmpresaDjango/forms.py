from django import forms
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from appEmpresaDjango.models import Departamento, Empleado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('index')


class DepartamentoUpdateView(UpdateView):
    model = Departamento
