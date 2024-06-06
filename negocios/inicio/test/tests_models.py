
from inicio.models import Equipo, OrdenServicio
from django.test import TestCase
from django.db import IntegrityError
from datetime import date


class TestEquipoOrdenServicio(TestCase):

    def test_crear_equipo(self):
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
        self.assertEqual(1, Equipo.objects.count())
        self.assertEqual(equipo.cliente_equipo, "Cliente 1")
        self.assertEqual(equipo.telefono_cliente, 1234567890)
        self.assertEqual(equipo.tipo_equipo, 'P')
        self.assertEqual(equipo.marca_equipo, "Marca 1")
        self.assertEqual(equipo.modelo_equipo, "Modelo 1")
        self.assertEqual(equipo.serial_number, "123456789")
        self.assertEqual(equipo.accesorios_equipo, "Cargador")
        self.assertEqual(equipo.contraseña_equipo, "password")
        self.assertEqual(equipo.sistema_operativo, "Windows 10")

    def test_crear_orden_servicio(self):
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
        self.assertEqual(1, OrdenServicio.objects.count())
        self.assertEqual(orden_servicio.fecha_orden, date.today())
        self.assertEqual(orden_servicio.cotizacion, 150.50)
        self.assertEqual(orden_servicio.tipo_servicio, "Reparación")
        self.assertEqual(orden_servicio.falla_equipo, "No enciende")
        self.assertEqual(
            orden_servicio.indicaciones_adicionales, "Revisar placa base")
        self.assertIsNone(orden_servicio.servicio_realizado)
        self.assertIsNone(orden_servicio.notas_finales)
        self.assertEqual(orden_servicio.encargado, "Técnico 1")
        self.assertEqual(orden_servicio.partes, "Placa base")
        self.assertIsNone(orden_servicio.fecha_entrega)
        self.assertEqual(orden_servicio.costo_final, 150.50)
        self.assertEqual(orden_servicio.observaciones_notas,
                         "Entregar urgentemente")
        self.assertEqual(orden_servicio.equipo, equipo)

    def test_equipo_serial_number_unique(self):
        Equipo.objects.create(
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

        with self.assertRaises(IntegrityError):
            Equipo.objects.create(
                cliente_equipo="Cliente 2",
                telefono_cliente=1234567891,
                tipo_equipo='P',
                marca_equipo="Marca 2",
                modelo_equipo="Modelo 2",
                serial_number="123456789",  # Repetido
                accesorios_equipo="Mouse",
                contraseña_equipo="password123",
                sistema_operativo="Windows 10"
            )

    def test_equipo_valor_por_defecto(self):
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente 1",
            telefono_cliente=1234567890,
            marca_equipo="Marca 1",
            modelo_equipo="Modelo 1",
            serial_number="123456789",
            sistema_operativo="Windows 10"
        )
        # Verifica que el valor por defecto es 'P'
        self.assertEqual(equipo.tipo_equipo, 'P')

    def test_fecha_entrega_nula(self):
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
        OrdenServicio.objects.create(
            fecha_orden=date.today(),
            cotizacion=150.50,
            tipo_servicio="Reparación",
            falla_equipo="No enciende",
            indicaciones_adicionales="Revisar placa base",
            equipo=equipo
        )
        self

    def test_str_method(self):
        equipo = Equipo.objects.create(
            cliente_equipo="Cliente de Prueba",
            telefono_cliente=123456789,
            tipo_equipo='P',
            marca_equipo="Marca de Prueba",
            modelo_equipo="Modelo de Prueba",
            serial_number="12345ABCDE",
            accesorios_equipo="Cargador, Mouse",
            contraseña_equipo="password123",
            sistema_operativo="Windows 10"
        )
        self.assertEqual(str(equipo), "Cliente de Prueba-12345ABCDE")
