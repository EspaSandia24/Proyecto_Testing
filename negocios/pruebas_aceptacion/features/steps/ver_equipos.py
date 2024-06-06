from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'presiono Equipos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="sidebar-nav"]/li[4]/a').click()
    time.sleep(1)


@when(u'presiono Lista de Equipos')
def step_impl(context):
    # Primero, verifica si el menú "Equipos" está colapsado y haz clic para expandirlo
    menu_equipos = context.driver.find_element(
        By.XPATH, "//a[@data-bs-target='#forms-nav']")
    if "collapsed" in menu_equipos.get_attribute("class"):
        menu_equipos.click()

    # Espera a que el menú se expanda y el enlace sea visible
    wait = WebDriverWait(context.driver, 3)
    lista_equipos = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[@href='/equipos/']")))

    # Haz clic en el enlace "Lista de Equipos"
    lista_equipos.click()


@then(u'se mostrara la Lista de Equipos que se tienen registrados')
def step_impl(context):
    Nombre = "Lista de Equipos"
    div = context.driver.find_element(By.XPATH, '//*[@id="main"]/h1')
    time.sleep(5)
    assert Nombre in div.text
