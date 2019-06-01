from django.urls import path

from . import views

app_name = 'servicios'
urlpatterns = [
    # ex: /servicios/
    path('', views.index, name='index'),
    # ex: /servicios/5/
    path('<int:servicio_id>/', views.detalle, name='detalle'),
    # ex: /servicios/nuevo_servicio
    path('nuevo/', views.nuevo_servicio, name='nuevo_servicio'),
    # ex: /servicios/3/editar
    path('<int:servicio_id>/editar/', views.editar_servicio, name='editar_servicio'),
    # ex: /servicios/3/eliminar
    path('<int:servicio_id>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    #
    path('<int:servicio_id>/finalizar/', views.finalizar_servicio, name='finalizar_servicio'),
    
    
    # ex: /servicios/tarea/5/
    path('tarea/<int:tarea_id>/', views.tarea, name='tarea'),
    # ex: /servicios/3/tarea/nueva
    path('<int:servicio_id>/tarea/nueva/', views.nueva_tarea, name='nueva_tarea'),
    # ex: /servicios/tarea/3/editar
    path('tarea/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    #
    path('tarea/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    #
    path('tarea/<int:tarea_id>/finalizar/', views.finalizar_tarea, name='finalizar_tarea'),
    
    # ex: /servicios/parte/5/
    path('parte/<int:parte_id>/', views.parte, name='parte'),
    # ex: /servicios/3/parte/nuevo
    path('<int:tarea_id>/parte/nuevo/', views.nuevo_parte, name='nuevo_parte'),
    # ex: /servicios/3/parte/jnuevo
    path('<int:tarea_id>/parte/jnuevo/', views.nuevo_parte_jefe, name='nuevo_parte_jefe'),
    # ex: /servicios/parte/3/editar
    path('parte/<int:parte_id>/editar/', views.editar_parte, name='editar_parte'),
    #
    path('parte/<int:parte_id>/eliminar/', views.eliminar_parte, name='eliminar_parte'),
    #
    path('parte/<int:parte_id>/aprobar/', views.aprobar_parte, name='aprobar_parte'),
    
    # ex: /servicios/cliente/2
    path('cliente/<int:cliente_id>/', views.cliente, name='cliente'),
    # ex: /servicios/clientes
    path('clientes/', views.clientes, name='clientes'),
    #  
    path('cliente/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    # 
    path('cliente/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    #
    path('cliente/<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    
    
    # ex: /servicios/empleado/4    
    path('empleado/<int:empleado_id>/', views.empleado, name='empleado'),
    #     
    path('empleado/<int:cuadrilla_id>/nuevo/', views.nuevo_empleado, name='nuevo_empleado'),
    #     
    path('empleado/<int:empleado_id>/editar', views.editar_empleado, name='editar_empleado'),
    #     
    path('empleado/<int:empleado_id>/eliminar', views.eliminar_empleado, name='eliminar_empleado'),
    
    # ex: /servicios/cuadrillas    
    path('cuadrillas/', views.cuadrillas, name='cuadrillas'),
    # ex: /servicios/cuadrilla/2
    path('cuadrilla/<int:cuadrilla_id>/', views.cuadrilla, name='cuadrilla'),
    #  
    path('cuadrilla/nueva/', views.nueva_cuadrilla, name='nueva_cuadrilla'),
    # 
    path('cuadrilla/<int:cuadrilla_id>/editar/', views.editar_cuadrilla, name='editar_cuadrilla'),
    #
    path('cuadrilla/<int:cuadrilla_id>/eliminar/', views.eliminar_cuadrilla, name='eliminar_cuadrilla'),
    #
    path('cuadrilla/<int:cuadrilla_id>/seleccionar_jefe/', views.seleccionar_jefe, name='seleccionar_jefe'),
    #
    path('cuadrilla/<int:cuadrilla_id>/seleccionar_jefe2/', views.seleccionar_jefe2, name='seleccionar_jefe2'),
    
        
]
