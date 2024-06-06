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
   tbody= tabla.context.driver.find_element(By.TAG_NAME,'tbody')
   rows=tbody.context.driver.find_element(By.TAG_NAME, 'tr')
   
   for row in rows:
        campos=row.context.driver.find_element(By.TAG_NAME, 'td')
        for campo in campos:
            if sn in campo.text:
                delete_button = row.find_element(By.CLASS_NAME, 'btn btn-danger')
                delete_button.click()
                return          
   
   
   

@then(u'el sistema mostrara las listas con el mensaje "{lista}"')
def step_impl(context,lista):
    head= context.driver.find_element(By.ID, 'main')
    time.sleep(5)
    assert lista in head
    