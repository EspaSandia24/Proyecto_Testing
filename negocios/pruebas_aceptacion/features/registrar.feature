Característica: Agregar Nuevo Usuario
Como AdminMCFistrador del sistema de Altas MFC
quiero registrar un nuevo usuario
para que pueda aceder al sistema.

Escenario: Usuario No Registrado
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Registrar Usuario
Y escribo el usuario "Pedro2" y su contraseña "1324" y confirmarmos la contraseña "1324"
Cuando presiono el boton de REGISTRAR
Entonces te manda a la pagina principal

Escenario: Datos Incompletos1
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Registrar Usuario
Y escribo la s contraseña "1324" y confirmarmos la contraseña "1324"
Cuando presiono el boton de REGISTRAR
Entonces se mostrara un mesaje de que "Por favor escoge un nombre de usuario."

Escenario: Datos Incompletos2
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Registrar Usuario
Y escribo el usuario "pedro" y confirmarmos la contraseña "1234"
Cuando presiono el boton de REGISTRAR
Entonces se mostrara el mesaje de que "Por favor ingresa tu contraseña!"

Escenario: Contraseñas No Iguales
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Registrar Usuario
Y escribo el usuario "Pedro2" y su contraseña "125" y confirmarmos la contraseña "123"
Cuando presiono el boton de REGISTRAR
Entonces no se registrara el usuario.