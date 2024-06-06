from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono Lista de Equipos')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="forms-nav"]/li[2]/a')


@when(u'presiono el botón eliminar con el numero de serie "{sn}"')
def step_impl(context,sn):
   tabla=context.driver.find_element(By.CLASS_NAME,'table')
   tbody= tabla.context.driver.find_element(By.CLASS_NAME,'tbody')
   

@then(u'el sistema mostrara las listas con el mensaje "Lista"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el sistema mostrara las listas con el mensaje "Lista"')