from django.test import TestCase
from django.contrib.auth.models import User,Group
from inicio.models import Equipo, OrdenServicio 
from datetime import date

class TestInicio(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='AdminMFC',
            email='regular_user@example.com',
            password='1234'
        )
        self.regular_user = User.objects.create_user(
            username='user1',
            email='regular_user@example.com',
            password='regular_password',
            is_active=True
        )
        self.technical_group = Group.objects.create(name='Tecnico')
        self.empelado_grupo = Group.objects.create(name='Empleado')

        # Asignar grupo inicial al usuario regular
        self.regular_user.groups.add(self.empelado_grupo)
        
    def test_login_status_200(self):
        response = self.client.get('')
        self.assertEqual(200,response.status_code)
        
    def test_iniciar_sesion(self):
        response = self.client.get('',{'username': 'AdminMFC', 'password': '1234'})
        self.assertEqual(200,response.status_code)
    
    def test_inicio_con_inicio_de_sesion(self):
        # Iniciar sesión con el usuario de prueba
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/principal/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_principal_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/principal/')
        self.assertEqual(200,response.status_code)    
    
    def test_agregar_equipo(self):
        self.client.login(username='AdminMFC', password='1234')
        response=self.client.post('/nuevoEquipo/',{'cliente_equipo': 'no se', 'telefono_cliente': '1234567891','tipo_equipo': 'P','marca_equipo': 'hp','modelo_equipo': '3ap2m','serial_number': '123ssa4a6a5s1','accesorios_equipo': 'ninguno','contraseña_equipo': '123','sistema_operativo': 'linux'})
        self.assertEqual(302,response.status_code)
    
    def test_agregar_equipo2(self):
        self.client.login(username='AdminMFC', password='1234')
        self.client.post('/nuevoEquipo/',{'cliente_equipo': "no se", 'telefono_cliente': 1234567891,'tipo_equipo': 'P','marca_equipo': "Marca 1",'modelo_equipo': "Modelo 1",'serial_number': "123ssa4a6a5s1",'accesorios_equipo': "ninguno",'contraseña_equipo': "123",'sistema_operativo': "linux"})
        self.assertEqual(1,Equipo.objects.count())
        
    def test_agregar_equipo_form_no_valido(self):
        self.client.login(username='AdminMFC', password='1234')
        response=self.client.post('/nuevoEquipo/',{'cliente_equipo': "no se", 'telefono_cliente': 1234567891,'tipo_equipo': 'Portatil','marca_equipo': "Marca 1",'modelo_equipo': "Modelo 1",'serial_number': "123ssa4a6a5s1",'accesorios_equipo': "ninguno",'contraseña_equipo': "123",'sistema_operativo': "linux"})
        self.assertEqual(200,response.status_code)
    
    
    def test_agregar_equipo_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoEquipo/')
        self.assertEqual(200,response.status_code)
        
    def test_agregar_orden_servicio(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        data = {
        'fecha_orden': "09/12/2023",
        'cotizacion': 150.50,
        'tipo_servicio': "limpieza",
        'falla_equipo': "ninguna",
        'indicaciones_adicionales': "sin indicaciones",
        'equipo': equipo.id  # Pass the 'equipo' object itself
         }

        
        response = self.client.post('/nuevoServicio/', data)
        self.assertEqual(302,response.status_code)
    
    def test_agregar_orden_servicio_form_no_valido(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        data = {
        'fecha_orden': "09/12/2023",
        'cotizacion': 150.50,
        'tipo_servicio': "limpieza",
        'falla_equipo': "ninguna",
        'indicaciones_adicionales': "sin indicaciones",
        'equipo': equipo # Pass the 'equipo' object itself
         }

        
        response = self.client.post('/nuevoServicio/', data)
        self.assertEqual(200,response.status_code)
        
        
    def test_agregar_orden_servicio_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoServicio/')
        self.assertEqual(200,response.status_code)
        
    def test_registar_usuario(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/registrar/',{'username': 'anita24', 'password': '1234','password2': '1234'})
        self.assertEqual(200,response.status_code)
        
    def test_creacion_usuario(self):
        self.client.login(username='AdminMFC', password='1234')
        self.client.post('/registrar/',{'username': 'anita24', 'password': '1234','password2': '1234'})
        self.assertEqual(User.objects.count(), 3)
        
    def test_creacion_usuario_usuario_ya_existente(self):
        self.client.login(username='AdminMFC', password='1234')
        self.client.post('/registrar/',{'username': 'user1', 'password': '1234','password2': '1234'})
        self.assertEqual(User.objects.count(), 2)
    
    def test_creacion_usuario_contraseña_diferente(self):
        self.client.login(username='AdminMFC', password='1234')
        response=self.client.post('/registrar/',{'username': 'useraa', 'password': '123','password2': '1234'})
        self.assertEqual(200,response.status_code)
        
    def test_registrar_usuarios_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/registrar/')
        self.assertEqual(200,response.status_code)
    
    def test_lista_usuarios_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/usuarios/')
        self.assertEqual(200,response.status_code)
        
    def test_eliminar_usuarios_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        user = User.objects.create_user(
            username='regular_user',
            email='regular_user@example.com',
            password='regular_password',
            is_active=True
        )
        response = self.client.get('/eliminar_usuario/'+str(user.id))
        self.assertEqual(302,response.status_code)
        
    def test_administrar_permisos(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.post('/tipo_usuario/'+str(self.regular_user.id), {'grupos': '{self.technical_group}'})
        self.assertEqual(302,response.status_code)
        
    def test_administrar_permisos_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/tipo_usuario/'+str(self.regular_user.id))
        self.assertEqual(200,response.status_code)
        

    def test_cerrar_sesion(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/logout/')
        self.assertEqual('/',response.url)
        
    def test_eliminar_equipo(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        response = self.client.get('/equipos/eliminarEquipo/'+str(equipo.id))
        self.assertEqual(302,response.status_code)  
        
    def test_editar_equipo(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        response = self.client.post('/equipos/editarEquipo/'+str(equipo.id),{'cliente_equipo': 'no se', 'telefono_cliente': '1234567891','tipo_equipo': 'P','marca_equipo': 'hp','modelo_equipo': '3ap2m','serial_number': '123ssa4a6a5s1','accesorios_equipo': 'ninguno','contraseña_equipo': '123','sistema_operativo': 'linux'})
        self.assertEqual(302,response.status_code)
        
    def test_editar_equipo_form_no_valido(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        response = self.client.post('/equipos/editarEquipo/'+str(equipo.id),{'cliente_equipo': 'no se', 'telefono_cliente': '1234567891','tipo_equipo': 'Paaa','marca_equipo': 'hp','modelo_equipo': '3ap2m','serial_number': '123ssa4a6a5s1','accesorios_equipo': 'ninguno','contraseña_equipo': '123','sistema_operativo': 'linux'})
        self.assertEqual(200,response.status_code)
        
    def test_editar_equipo_status(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        response = self.client.get('/equipos/editarEquipo/'+str(equipo.id))
        self.assertEqual(200,response.status_code)
        
    def test_lista_equipo_status(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        response = self.client.get('/equipos/')
        self.assertEqual(200,response.status_code)
        
        
    def test_eliminar_orden(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        orden_servicio = OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            servicio_realizado=None,
            notas_finales=None,
            encargado="Técnico 1",
            partes="Placa base",
            fecha_entrega=None,
            costo_final=150.50,
            observaciones_notas="Entregar urgentemente",
            equipo=equipo
        )
        response = self.client.get('/servicios/eliminarOrden/'+str(orden_servicio.id_orden))
        self.assertEqual(302,response.status_code)  
        
        
    def test_editar_orden(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        orden_servicio = OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            servicio_realizado=None,
            notas_finales=None,
            encargado="Técnico 1",
            partes="Placa base",
            fecha_entrega=None,
            costo_final=150.50,
            observaciones_notas="Entregar urgentemente",
            equipo=equipo
        )
        response = self.client.post('/servicios/editarOrden/'+str(orden_servicio.id_orden),{'fecha_entrega': '09/12/2023', 'cotizacion': '123','costo_final': '123','tipo_servicio': 'limpieza','falla_equipo': 'ninguna','indicaciones_adicionales': 'sin indicaciones','servicio_realizado':'limpieza profunda', 'notas_finales':'lista para entrega','encargado':'EspaSandia24','observaciones_notas':'ninguna','partes':'ninguna'})
        self.assertEqual(302,response.status_code)
        
    def test_editar_orden_form_no_valido(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        orden_servicio = OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            servicio_realizado=None,
            notas_finales=None,
            encargado="Técnico 1",
            partes="Placa base",
            fecha_entrega=None,
            costo_final=150.50,
            observaciones_notas="Entregar urgentemente",
            equipo=equipo
        )
        response = self.client.post('/servicios/editarOrden/'+str(orden_servicio.id_orden),{'fecha_entrega': '09/12/', 'cotizacion': '123','costo_final': '123','tipo_servicio': 'limpieza','falla_equipo': 'ninguna','indicaciones_adicionales': 'sin indicaciones','servicio_realizado':'limpieza profunda', 'notas_finales':'lista para entrega','encargado':'EspaSandia24','observaciones_notas':'ninguna','partes':'ninguna'})
        self.assertEqual(200,response.status_code)
        
    def test_editar_orden_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        orden_servicio = OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            servicio_realizado=None,
            notas_finales=None,
            encargado="Técnico 1",
            partes="Placa base",
            fecha_entrega=None,
            costo_final=150.50,
            observaciones_notas="Entregar urgentemente",
            equipo=equipo
        )
        response = self.client.get('/servicios/editarOrden/'+str(orden_servicio.id_orden))
        self.assertEqual(200,response.status_code)
        
    def test_lista_orden_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            tipo_equipo='P',
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            accesorios_equipo="Cargador",
            contraseña_equipo="password",
            sistema_operativo="Windows 10"
        )
        orden_servicio = OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            servicio_realizado=None,
            notas_finales=None,
            encargado="Técnico 1",
            partes="Placa base",
            fecha_entrega=None,
            costo_final=150.50,
            observaciones_notas="Entregar urgentemente",
            equipo=equipo
        )
        response = self.client.get('/servicios/')
        self.assertEqual(200,response.status_code)