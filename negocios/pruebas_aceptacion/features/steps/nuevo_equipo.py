from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
@given(u'presiono Nuevo Equipo')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="forms-nav"]/li[1]/a').click()
    time.sleep(1)
    
@given(u'escribo el Cliente "{nombre}" y su telefono "{telefono}"')
def step_impl(context, nombre, telefono):
   context.driver.find_element(By.NAME, 'cliente_equipo').send_keys(nombre)
   context.driver.find_element(By.NAME, 'telefono_cliente').send_keys(telefono)
   time.sleep(1)


@given(u'selecciono en el tipo de equipo "{tipo}"')
def step_impl(context,tipo):
    context.driver.find_element(By.NAME, 'tipo_equipo').send_keys(tipo)
    time.sleep(1)

@given(u'escribo la marca "{marca}" y el modelo "{modelo}"')
def step_impl(context, marca, modelo):
    context.driver.find_element(By.NAME, 'marca_equipo').send_keys(marca)
    context.driver.find_element(By.NAME, 'modelo_equipo').send_keys(modelo)
    time.sleep(1)

@given(u'el numero serial "{sn}" y los accesorios "{acce}"')
def step_impl(context,sn,acce):
    context.driver.find_element(By.NAME, 'serial_number').send_keys(sn)
    context.driver.find_element(By.NAME, 'accesorios_equipo').send_keys(acce)
    time.sleep(1)

@given(u'la contraseña "{clave}" y el sistema operativo "{SO}"')
def step_impl(context,clave,SO):
    context.driver.find_element(By.NAME, 'contraseña_equipo').send_keys(clave)
    context.driver.find_element(By.NAME, 'sistema_operativo').send_keys(SO)
    time.sleep(1)


@when(u'presiono el botón Agregar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="main"]/form/button').click()
    time.sleep(1)


@then(u'el sistema mostrara el mensaje "{sn}"')
def step_impl(context,sn):
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(1)
    assert sn in div.text
    
@then(u'el sistema muestra el mensaje "{mensaje}"')
def step_impl(context,mensaje):
    error = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    time.sleep(1)
    assert mensaje in error.text
    
@given(u'escribo el Cliente "{nm}"')
def step_impl(context,nm):
    context.driver.find_element(By.NAME, 'cliente_equipo').send_keys(nm)


@then(u'el sistema no deja guardar y te muestra el mensaje "{NE}"')
def step_impl(context,NE):
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(1)
    assert NE in div.text