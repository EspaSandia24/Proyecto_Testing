Característica: Dar permisos a los usuarios
Como administrador del sistema de Altas MFC
quiero asignar permisos a los usuarios en base a su rango, 
para que puedan realizar sus actividades correspondientes.

Escenario: Cambiar permiso a Empleado
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Permisos
Y se mostra la Lista de Usuarios
Y le da click al botón Cambiar Permisos a un usuario
Y de la lista de Permisos elije Empleado
Cuando le da click al botón Cambiar
Entonces nos muestra la Lista de Usuarios con el Permiso del usuario cambiado a Empleado