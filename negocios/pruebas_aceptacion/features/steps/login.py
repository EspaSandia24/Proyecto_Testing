from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@given(u'escribo mi Usuario "{Usuario}" y mi Password "{Password}"')
def step_impl(context, Usuario, Password):
    context.driver.find_element(By.NAME, 'username').send_keys(Usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(Password)

@when(u'presiono el botón Login')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[3]/button').click()


@then(u'puedo ver "{Nombre}" en el Dashboard')
def step_impl(context, Nombre):
   div = context.driver.find_element(By.ID, 'main')
   time.sleep(5)
   assert Nombre in div.text, f"El usuario {Nombre} no se encuentra en {div.text}"