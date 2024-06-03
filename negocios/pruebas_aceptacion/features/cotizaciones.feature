Característica: Agregar Cotizaciones
Como usuario del sistema de Altas MFC
quiero poner cotizaciones al equipo que estoy revisando
poder llevar un registro de esta información y otorgar al cliente.

Escenario: Datos Correctos
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Nueva Orden De Servicio
Y escribo la fecha "03/06/2024" y la cotizacion "1324" y  el tipo de servicio "mantenimiento" y la falla "ninguna" las indicaciones  "ninguna" y el equipo "pepe-845552455115524"
Cuando presiono el boton de Agregar
Entonces te manda a la lista de las ordenes

Escenario: Datos incompletos cotizacion
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Nueva Orden De Servicio
Y escribo la fecha "03/06/2024" y  el tipo de servicio "mantenimiento" y la falla "ninguna" las indicaciones  "ninguna" y el equipo "pepe-845552455115524"
Cuando presiono el boton de Agregar
Entonces no nos dejara agregar la orden

Escenario: Datos incorrectos cotizacion
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Nueva Orden De Servicio
Cuando escribo la fecha "03/06/2024" y la cotizacion "aaa" y  el tipo de servicio "mantenimiento" y la falla "ninguna" las indicaciones  "ninguna" y el equipo "pepe-845552455115524" 
Entonces el campo de la cotizacion quedara vacio