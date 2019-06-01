from django.contrib import admin

from .models import Servicio, Cliente, Tarea, EmpleadoDeCuadrilla, Cuadrilla, ParteDeTrabajo 

admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Tarea)
admin.site.register(EmpleadoDeCuadrilla)
admin.site.register(Cuadrilla)
admin.site.register(ParteDeTrabajo)
