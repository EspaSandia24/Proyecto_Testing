Característica: Agregar notas
Como usuario del sistema de Altas MFC
quiero poner notas sobre el avance de la revisión de un equipo
poder darle información a un cliente que pregunta por su equipo.

Escenario: Agregar notas Datos incompletos 1
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añaden las partes del equipo a revisar "Una RAM"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos incompletos 2
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añaden las partes del equipo a revisar "Una RAM"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos incompletos 3
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añaden las partes del equipo a revisar "Una RAM"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos incompletos 4
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añaden las partes del equipo a revisar "Una RAM"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos incompletos 5
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos incompletos 6
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añaden las partes del equipo a revisar "Una RAM"
Cuando le da click al botón Guardar
Entonces no nos dejara guardar la orden

Escenario: Agregar notas Datos completos 
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234"
Y presiono el botón Login 
Y dirijete Menu
Y presiono Orden De Servicio
Y presiono Lista De Ordenes De Servicio
Y se mostra la lista con las notas 
Y le da click al botón Editar
Y se le añade el Servicio que se está realizando al equipo "Cambio de RAM"
Y escribe la nota en el campo de Obeservaciones "Se está buscando la pieza"
Y se escribe alguna nota final "La ram recomendada es de 16"
Y se le añade el nombre del Encargado del servicio "Pedro"
Y se le añaden las partes del equipo a revisar "Una RAM"
Y se le añade el Costo final "1500"
Cuando le da click al botón Guardar
Entonces el sistema te manda a la lista de las Ordenes de Servicio