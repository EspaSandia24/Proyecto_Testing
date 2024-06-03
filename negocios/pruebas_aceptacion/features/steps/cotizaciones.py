from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono Orden De Servicio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="sidebar-nav"]/li[3]/a').click()
    time.sleep(2)

@given(u'presiono Nueva Orden De Servicio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="components-nav"]/li[1]/a').click()



@given(u'escribo la fecha "{fecha}" y la cotizacion "{cotizacion}" y  el tipo de servicio "{servicio}" y la falla "{falla}" las indicaciones  "{indicaciones}" y el equipo "{equipo}"')
def step_impl(context,fecha,cotizacion,servicio,falla,indicaciones,equipo):
    context.driver.find_element(By.NAME, 'fecha_orden').send_keys(fecha)
    context.driver.find_element(By.NAME, 'cotizacion').send_keys(cotizacion)
    context.driver.find_element(By.NAME, 'tipo_servicio').send_keys(servicio)
    context.driver.find_element(By.NAME, 'falla_equipo').send_keys(falla)
    context.driver.find_element(By.NAME, 'indicaciones_adicionales').send_keys(indicaciones)
    context.driver.find_element(By.NAME, 'equipo').send_keys(equipo)


@when(u'presiono el boton de Agregar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="main"]/form/button').click()
    

@then(u'te manda a la lista de las ordenes')
def step_impl(context):
    Nombre="Lista de Ordenes de Servicios"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text
    
@given(u'escribo la fecha "{fecha}" y  el tipo de servicio "{servicio}" y la falla "{falla}" las indicaciones  "{indicaciones}" y el equipo "{equipo}"')
def step_impl(context,fecha,servicio,falla,indicaciones,equipo):
    context.driver.find_element(By.NAME, 'fecha_orden').send_keys(fecha)
    context.driver.find_element(By.NAME, 'tipo_servicio').send_keys(servicio)
    context.driver.find_element(By.NAME, 'falla_equipo').send_keys(falla)
    context.driver.find_element(By.NAME, 'indicaciones_adicionales').send_keys(indicaciones)
    context.driver.find_element(By.NAME, 'equipo').send_keys(equipo)

@then(u'no nos dejara agregar la orden')
def step_impl(context):
    Nombre="Nueva Orden de Servicio"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text
    
@when(u'escribo la fecha "{fecha}" y la cotizacion "{cotizacion}" y  el tipo de servicio "{servicio}" y la falla "{falla}" las indicaciones  "{indicaciones}" y el equipo "{equipo}"')
def step_impl(context,fecha,cotizacion,servicio,falla,indicaciones,equipo):
    context.driver.find_element(By.NAME, 'fecha_orden').send_keys(fecha)
    context.driver.find_element(By.NAME, 'cotizacion').send_keys(cotizacion)
    context.driver.find_element(By.NAME, 'tipo_servicio').send_keys(servicio)
    context.driver.find_element(By.NAME, 'falla_equipo').send_keys(falla)
    context.driver.find_element(By.NAME, 'indicaciones_adicionales').send_keys(indicaciones)
    context.driver.find_element(By.NAME, 'equipo').send_keys(equipo)
    time.sleep(5)
    

@then(u'el campo de la cotizacion quedara vacio')
def step_impl(context):
    div = context.driver.find_element(By.XPATH, '//*[@id="id_cotizacion"]')
    if not div.text:
        print("El elemento está vacío.")
    else:
        print(f"El elemento contiene: {div.text}")
    context.driver.quit()