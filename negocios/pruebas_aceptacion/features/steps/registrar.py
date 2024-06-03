from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'presiono el botón Login')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[3]/button').click()
    time.sleep(2)

@given(u'dirijete Menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/i').click()
    time.sleep(2)



@given(u'presiono Registrar Usuario')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="sidebar-nav"]/li[7]/a').click()
    time.sleep(3)


@given(u'escribo el usuario "{Usuario}" y su contraseña "{Password}" y confirmarmos la contraseña "{Password2}"')
def step_impl(context,Usuario,Password,Password2):
    context.driver.find_element(By.NAME, 'username').send_keys(Usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(Password)
    context.driver.find_element(By.NAME, 'password2').send_keys(Password2)
    

@when(u'presiono el boton de REGISTRAR')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[4]/button').click()


@then(u'te manda a la pagina principal')
def step_impl(context):
    Nombre="MFC, Servicios de Computo"
    div = context.driver.find_element(By.ID, 'main')
    time.sleep(5)
    assert Nombre in div.text, f"El usuario {Nombre} no se encuentra en {div.text}"
    
    
@given(u'escribo la s contraseña "{Password}" y confirmarmos la contraseña "{Password2}"')
def step_impl(context,Password,Password2):
    context.driver.find_element(By.NAME, 'password').send_keys(Password)
    context.driver.find_element(By.NAME, 'password2').send_keys(Password2)
    
@then(u'se mostrara un mesaje de que "{mensaje}"')
def step_impl(context,mensaje):
    div = context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[1]/div/div')
    time.sleep(5)
    assert mensaje in div.text, f"El usuario {mensaje} no se encuentra en {div.text}"
    
    
@given(u'escribo el usuario "{usuario}" y confirmarmos la contraseña "{password}"')
def step_impl(context,usuario,password):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    
    context.driver.find_element(By.NAME, 'password2').send_keys(password)
    
@then(u'no se registrara el usuario.')
def step_impl(context):
    Nombre="Registrar Usuarios"
    div = context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/div/h5')
    time.sleep(5)
    assert Nombre in div.text, f"El usuario {Nombre} no se encuentra en {div.text}"
    
@then(u'se mostrara el mesaje de que "{mensaje}"')
def step_impl(context,mensaje):
    div = context.driver.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div[2]/div/form/div[2]/div')
    time.sleep(5)
    assert mensaje in div.text, f"El usuario {mensaje} no se encuentra en {div.text}"