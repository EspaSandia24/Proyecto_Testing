Característica: Agregar Un Equipo Nuevo
Como usuario del sistema Altas MFC 
quiero guardar la información de los equipos nuevos que llegan
para poder realizar mis actividades.

Escenario: Datos Correctos
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234" 
Y presiono el botón Login 
Y dirijete Menu
Y presiono Equipos
Y presiono Nuevo Equipo
Y escribo el Cliente "Liz" y su telefono "4921199113"
Y selecciono en el tipo de equipo "portatil"
Y escribo la marca "HP" y el modelo "Victus 16"
Y el numero serial "A45T32" y los accesorios "Pantalla"
Y la contraseña "L261901" y el sistema operativo "Windows 11"
Cuando presiono el botón Agregar
Entonces el sistema mostrara el mensaje "Lista de Equipos" 

Escenario: SN duplicado
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234" 
Y presiono el botón Login 
Y dirijete Menu
Y presiono Equipos
Y presiono Nuevo Equipo
Y escribo el Cliente "Liz" y su telefono "4921199113"
Y selecciono en el tipo de equipo "portatil"
Y escribo la marca "HP" y el modelo "Victus 16"
Y el numero serial "A45T32" y los accesorios "Pantalla"
Y la contraseña "L261901" y el sistema operativo "Windows 11"
Cuando presiono el botón Agregar
Entonces el sistema muestra el mensaje "Equipo with this Serial number already exists." 

Escenario: Datos incompletos
Dado que ingreso a la url "http://192.168.33.10:8000/"
Y escribo mi usuario "AdminMFC" y mi Password "1234" 
Y presiono el botón Login 
Y dirijete Menu
Y presiono Equipos
Y presiono Nuevo Equipo
Y escribo el Cliente "Liz"
Y selecciono en el tipo de equipo "portatil"
Y escribo la marca "HP" y el modelo "Victus 16"
Y el numero serial "A45T32" y los accesorios "Pantalla"
Y la contraseña "L261901" y el sistema operativo "Windows 11"
Cuando presiono el botón Agregar
Entonces el sistema no deja guardar y te muestra el mensaje "Nuevo Equipo"