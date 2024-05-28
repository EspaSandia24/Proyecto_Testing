from django.urls import path
from inicio import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.LoginView.as_view(), name='IniciarSesion'),
    path('registrar/', views.registrar, name='Registrar'),
    path('principal/', views.incio, name='Principal'),
    path('equipos/', views.lista_equipos, name='Equipos'),
    path('nuevoEquipo/', views.agregar_equipo, name='nuevoEquipo'),
    path('servicios/', views.lista_servicios, name='Servicios'),
    path('nuevoServicio/', views.agregar_servicio, name='nuevoServicio'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('servicios/eliminarOrden/<int:id_orden>', views.eliminar_orden, name='eliminarOrden'),
    path('servicios/editarOrden/<int:id_orden>', views.editar_orden, name='editarOrden'),
    path('equipos/eliminarEquipo/<int:serial_number>', views.eliminar_equipo, name='eliminarEquipo'),
    path('equipos/editarEquipo/<int:serial_number>', views.editar_equipo, name='editarEquipo'),   
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('tipo_usuario/<int:id>', views.asignar_grupo, name='asignarGrupo'),   
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminarUsuario'),   
       
]
