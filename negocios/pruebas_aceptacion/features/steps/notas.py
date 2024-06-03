from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@when(u'presiono Lista De Ordenes De Servicio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="components-nav"]/li[2]/a/span').click()


@then(u'se mostrara la lista con las notas')
def step_impl(context):
    Nombre="Notas Finales"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/table/thead/tr/th[5]')
    time.sleep(5)
    assert Nombre in div.text