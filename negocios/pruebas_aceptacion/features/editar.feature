Característica: Editar
Como usuario del sistema Altas MFC 
quiero poder editar los equipos y ordenes
para tener la información correcta

Escenario: Editar equipo
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234" 
Y presiono el botón Login 
Y dirijete Menu
Y presiono Equipos
Y presiono Lista de Equipos
Y presiono el botón editar con el numero de serie "A45789"
Y cambio el valor del modelo a "Victus 15"
Cuando presiono el boton Guardar
Entonces el sistema mostrara las listas con el mensaje "Lista"