from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono Lista de Equipos')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/aside/ul/li[4]/ul/li[2]/a')


@when(u'presiono el botón eliminar')
def step_impl(context):
   context.driver.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr[1]/td[7]/a').click()      
   
   

@then(u'el sistema mostrara las listas con el mensaje "{lista}"')
def step_impl(context,lista):
    head= context.driver.find_element(By.ID, 'main')
    time.sleep(5)
    assert lista in head
    