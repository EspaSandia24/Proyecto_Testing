from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)


@given(u'escribo mi Usuario "{Usuario}" y mi Password "{Password}"')
def step_impl(context, Usuario, Password):
    context.driver.find_element(By.NAME, 'username').send_keys(Usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(Password)
    time.sleep(2)


@when(u'presiono el botón Login')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[3]/button').click()
    time.sleep(2)


@then(u'puedo ver "{mensaje}"')
def step_impl(context, mensaje):
    div = context.driver.find_element(By.ID, 'main')
    time.sleep(5)
    assert mensaje in div.text


@then(u'la pagina se recarga mostrando el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    body = context.driver.find_element(By.CLASS_NAME, 'card-body')
    time.sleep(5)
    assert mensaje in body.text
