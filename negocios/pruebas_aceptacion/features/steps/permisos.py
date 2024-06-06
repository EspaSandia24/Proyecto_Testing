from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


@given(u'presiono Permisos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="sidebar-nav"]/li[6]/a').click()
    time.sleep(1)


@given(u'se mostra la Lista de Usuarios')
def step_impl(context):
    Nombre = "Lista de Usuarios"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text


@given(u'le da click al botón Cambiar Permisos a un usuario')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, "//a[contains(@class, 'btn-warning') and contains(text(), 'Cambiar Permiso')]").click()


@given(u'de la lista de Permisos elije Empleado')
def step_impl(context):
    select_element = context.driver.find_element(By.NAME, 'grupo')
    select = Select(select_element)
    select.select_by_value('3')


@when(u'le da click al botón Cambiar')
def step_impl(context):
    time.sleep(2)
    boton_guardar = context.driver.find_element(
        By.XPATH, "//button[@type='submit' and contains(text(), 'Cambiar')]")
    context.driver.execute_script(
        "arguments[0].scrollIntoView(true);", boton_guardar)
    time.sleep(1)
    boton_guardar.click()


@then(u'nos muestra la Lista de Usuarios con el Permiso del usuario cambiado a Empleado')
def step_impl(context):
    Nombre = "Lista de Usuarios"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text
