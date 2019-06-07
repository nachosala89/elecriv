from django import forms

from .models import Servicio, Tarea, ParteDeTrabajo, Cliente, Cuadrilla, EmpleadoDeCuadrilla


class NicerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NicerForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control w-25"
                })


class ServicioForm(NicerForm):

    class Meta:
        model = Servicio
        fields = ('descripcion', 'cliente', 'fecha_solcitud', 'fecha_inicio', 'fecha_fin', 'estado', 'fecha_fin',)
        

class TareaForm(NicerForm):

    class Meta:
        model = Tarea
        fields = ('descripcion', 'servicio', 'estado', 'cuadrilla')
        

class ParteForm(NicerForm):

    class Meta:
        model = ParteDeTrabajo
        fields = ('descripcion', 'tarea', 'fecha')
        

class ClienteForm(NicerForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'descripcion', 'telefono')
        
        
class CuadrillaForm(NicerForm):

    class Meta:
        model = Cuadrilla
        fields = ('especialidad', 'vehiculo')
        
        
class EmpleadoForm(NicerForm):

    class Meta:
        model = EmpleadoDeCuadrilla
        fields = ('legajo', 'cuil', 'cuadrilla', 'nombre', 'apellido', 'empleado_desde', 'fecha_nac', 'es_jefe')
