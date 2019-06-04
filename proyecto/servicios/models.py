from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('En curso', 'En curso'),
        ('Finalizado', 'Finalizado'),    
    )    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    fecha_solcitud = models.DateField('fecha de solicitud')
    fecha_inicio = models.DateField('fecha de inicio', blank=True, null=True)
    fecha_fin = models.DateField('fecha de fin', blank=True, null=True)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=12, choices=ESTADOS)
    

    def __str__(self):
        return self.descripcion


class Cuadrilla(models.Model):
    especialidad = models.CharField(max_length=100)
    vehiculo = models.CharField(max_length=50)
    def jefe(self):
        return self.empleadodecuadrilla_set.get(es_jefe=True)

    def __str__(self):
        return self.especialidad


class Tarea(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)    
    descripcion = models.CharField(max_length=200)
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('En curso', 'En curso'),
        ('Finalizado', 'Finalizado'),    
    )    
    estado = models.CharField(max_length=12, choices=ESTADOS)
    cuadrilla = models.ForeignKey(Cuadrilla, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descripcion


class EmpleadoDeCuadrilla(models.Model):
    legajo = models.IntegerField(default=0)
    cuil = models.CharField(max_length=13)
    cuadrilla = models.ForeignKey(Cuadrilla, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    empleado_desde = models.DateField('empleado desde')
    fecha_nac = models.DateField('fecha de nacimiento')
    es_jefe = models.BooleanField('es jefe de cuadrilla', default=False)
    
    def __str__(self):
        return self.apellido


class ParteDeTrabajo(models.Model):
    fecha = models.DateField()
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    aprobado_por = models.ForeignKey(EmpleadoDeCuadrilla, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.descripcion

