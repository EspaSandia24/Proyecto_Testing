from behave import given, when
from selenium.webdriver.common.by import By


@given(u'presiono el botón editar con el numero de serie "{sn}"')
def step_impl(context, sn):
    tabla = context.driver.find_element(By.CLASS_NAME, 'table')
    tbody = tabla.context.driver.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.context.driver.find_element(By.TAG_NAME, 'tr')

    for row in rows:
        campos = row.context.driver.find_element(By.TAG_NAME, 'td')
        for campo in campos:
            if sn in campo.text:
                editar_button = row.find_element(
                    By.CLASS_NAME, 'btn btn-success')
                editar_button.click()


@given(u'cambio el valor del modelo a "{modelo}"')
def step_impl(context, modelo):
    context.driver.find_element(By.NAME, 'modelo_equipo')


@when(u'presiono el boton Guardar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="main"]/form/button')
