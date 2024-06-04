from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono Lista De Ordenes De Servicio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="components-nav"]/li[2]/a/span').click()


@given(u'se mostra la lista con las notas')
def step_impl(context):
    Nombre="Notas Finales"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/table/thead/tr/th[5]')
    time.sleep(5)
    assert Nombre in div.text


@given(u'le da click al botón Editar')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(), 'Editar')]").click()



@given(u'se le añade el Servicio que se está realizando al equipo "{servicio}"')
def step_impl(context, servicio):
    context.driver.find_element(By.NAME, 'servicio_realizado').send_keys(servicio)

@given(u'se escribe alguna nota final "{notaFinal}"')
def step_impl(context, notaFinal):
    context.driver.find_element(By.NAME, 'notas_finales').send_keys(notaFinal)

@given(u'se le añade el nombre del Encargado del servicio "{nombre}"')
def step_impl(context,nombre):
    context.driver.find_element(By.NAME, 'encargado').send_keys(nombre)

@given(u'se le añaden las partes del equipo a revisar "{parte}"')
def step_impl(context,parte):
    context.driver.find_element(By.NAME, 'partes').send_keys(parte)

@given(u'se le añade el Costo final "{costo}"')
def step_impl(context, costo):
    context.driver.find_element(By.NAME, 'costo_final').send_keys(costo)

@given(u'escribe la nota en el campo de Obeservaciones "{observaciones}"')
def step_impl(context, observaciones): 
    context.driver.find_element(By.NAME, 'observaciones_notas').send_keys(observaciones)


@when(u'le da click al botón Guardar')
def step_impl(context):
    # Esperar un poco para asegurarse de que el botón está cargado y visible
    time.sleep(5)  # Ajusta este tiempo según sea necesario
    
    boton_guardar = context.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Guardar')]")
    
    # Desplazarse hasta el botón
    context.driver.execute_script("arguments[0].scrollIntoView(true);", boton_guardar)
    
    # Esperar un poco para asegurarse de que el botón está visible
    time.sleep(1)  # Ajusta este tiempo según sea necesario
    
    # Hacer clic en el botón
    boton_guardar.click()


@then(u'el sistema te manda a la lista de las Ordenes de Servicio')
def step_impl(context):
    Nombre="Notas Finales"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/table/thead/tr/th[5]')
    time.sleep(5)
    assert Nombre in div.text

@then(u'no nos dejara guardar la orden')
def step_impl(context):
    Nombre="Editar Orden de Servicio"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text