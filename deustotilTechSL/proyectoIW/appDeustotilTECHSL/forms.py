from django import forms
from .models import Proyecto, Tarea, Empleado, Cliente


class DateInput(forms.DateInput):
    input_type = 'date'


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class ModificarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class ModificarTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        exclude = ['nota_adicional']
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class UpdateNotaTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('nota_adicional',)


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
