from django import forms

from .models import Servicio, Tarea, ParteDeTrabajo, Cliente, Cuadrilla, EmpleadoDeCuadrilla


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('descripcion', 'cliente', 'fecha_solcitud', 'fecha_inicio', 'fecha_fin', 'estado', 'fecha_fin',)
        

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ('descripcion', 'servicio', 'estado',)
        

class ParteForm(forms.ModelForm):

    class Meta:
        model = ParteDeTrabajo
        fields = ('descripcion', 'tarea', 'fecha', 'aprobado_por')

class ParteJefeForm(forms.ModelForm):

    class Meta:
        model = ParteDeTrabajo
        fields = ('descripcion', 'tarea', 'fecha')
        

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'descripcion', 'telefono')
        
        
class CuadrillaForm(forms.ModelForm):

    class Meta:
        model = Cuadrilla
        fields = ('especialidad', 'vehiculo')
        
        
class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = EmpleadoDeCuadrilla
        fields = ('legajo', 'cuil', 'cuadrilla', 'nombre', 'apellido', 'empleado_desde', 'fecha_nac', 'es_jefe')

