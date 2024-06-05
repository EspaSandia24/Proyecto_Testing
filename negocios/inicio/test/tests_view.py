from django.test import TestCase
from django.contrib.auth.models import User,Group
from django.urls import reverse

class TestInicio(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='AdminMFC',
            email='regular_user@example.com',
            password='1234'
        )
        self.regular_user = User.objects.create_user(
            username='regular_user',
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
        
    def test_agregar_equipo(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoEquipo/',{'cliente_equipo': 'no se', 'telefono_cliente': '123','tipo_equipo': 'Portatil','marca_equipo': 'hp','modelo_equipo': '3ap2m','serial_number': '123ssa4a6a5s1','accesorios_equipo': 'ninguno','contraseña_equipo': '123','sistema_operativo': 'linux'})
        self.assertEqual(200,response.status_code)
    
    def test_agregar_equipo_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoEquipo/')
        self.assertEqual(200,response.status_code)
        
    def test_agregar_orden_servicio(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoServicio/',{'fecha_orden': '09/12/2023', 'cotizacion': '123','tipo_servicio': 'limpieza','falla_equipo': 'ninguna','indicaciones_adicionales': 'sin indicaciones','equipo':'pepe-845552455115524'})
        self.assertEqual(200,response.status_code)
        
    def test_agregar_orden_servicio_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/nuevoServicio/')
        self.assertEqual(200,response.status_code)
        
    def test_registar_usuario(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/registrar/',{'username': 'anita24', 'password': '1234','password2': '1234'})
        self.assertEqual(200,response.status_code)
        
    def test_registrar_usuarios_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/registrar/')
        self.assertEqual(200,response.status_code)
        
    def test_administrar_permisos(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/tipo_usuario/'+str(self.regular_user.id), {'grupos': '{self.technical_group}'})
        self.assertEqual(200,response.status_code)
        
    def test_administrar_permisos_status_200(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/tipo_usuario/'+str(self.regular_user.id))
        self.assertEqual(200,response.status_code)
        

    def test_cerrar_sesion(self):
        self.client.login(username='AdminMFC', password='1234')
        response = self.client.get('/logout/')
        self.assertEqual('/',response.url)