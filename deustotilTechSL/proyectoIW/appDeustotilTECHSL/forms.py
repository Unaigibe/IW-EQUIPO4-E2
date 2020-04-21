from django import forms
from .models import Proyecto, Tarea, Empleado, Cliente


# Creacion de la clase DateInput para poder emplear widgets de fechas en algunos campos de los modelos.
# Esto facilita su creacion/modificacion en los formularios de dichos objetos
class DateInput(forms.DateInput):
    input_type = 'date'


# Formulario de Proyecto con todos los campos.
# Para los campos de fechas, se emplean widgets de fechas.
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


# Formulario para modificar un Proyecto con todos los campos.
# Para los campos de fechas, se emplean widgets de fechas.
class ModificarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


# Formulario de Tarea con todos los campos.
# Para los campos de fechas, se emplean widgets de fechas.
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


# Formulario para modificar una Tarea con todos los campos menos nota_adicional.
# Para los campos de fechas, se emplean widgets de fechas.
class ModificarTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        exclude = ['nota_adicional']
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


# Formulario para modificar el campo nota_adicional de una tarea.
class UpdateNotaTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('nota_adicional',)


# Formulario de Empleado con todos los campos.
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


# Formulario de Cliente con todos los campos.
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
