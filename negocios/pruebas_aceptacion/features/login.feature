Característica: Iniciar sesión
Como usuario del sistema Altas MFC
quiero iniciar sesión 
para poder realizar mis acitividades.

Escenario: Credenciales Validas
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi Usuario "AdminMFC" y mi Password "1234"
Cuando presiono el botón Login 
Entonces puedo ver "MFC, Servicios de Computo" 

Escenario: Credenciales No Validas
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi Usuario "Ulises" y mi Password "A19U20"
Cuando presiono el botón Login 
Entonces la pagina se recarga mostrando el mensaje "Ingresa a tu cuenta" 
