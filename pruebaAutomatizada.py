from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Configuración del WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Crear un directorio para los screenshots si no existe
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

def take_screenshot(step_name):
    """Función para tomar screenshots y guardarlos."""
    driver.save_screenshot(f"{screenshot_dir}/{step_name}.png")

# Acceder a la página de registro
driver.get("file:///C:/Users/jergarcia/Downloads/proyectoFinal_prog3/proyecto_final_prog3/index.html")
take_screenshot("1_registro")

# Rellenar el formulario de registro
email_input = file:///C:/Users/jergarcia/Downloads/proyectoFinal_prog3/proyecto_final_prog3/index.htmldriver.driver.find_element(By.XPATH, "//a[@href=/20210055-2024/Aplicaci%C3%B3n%20de%20Gesti%C3%B3n%20de%20Tareas/_workitems/edit/7/']")
password_input = driver.find_element(By.XPATH, "//a[@href='/20210055-2024/Aplicaci%C3%B3n%20de%20Gesti%C3%B3n%20de%20Tareas/_workitems/edit/7/']")

email_input.send_keys("registro_prueba@gmail.com.do")
password_input.send_keys("A*12345678")

# Enviar el formulario de registro
registro_button = driver.find_element(By.XPATH, "//a[@href='/20210055-2024/Aplicaci%C3%B3n%20de%20Gesti%C3%B3n%20de%20Tareas/_workitems/edit/7/']")
registro_button.click()
take_screenshot("2_registro_completado")

# Verificar el registro exitoso
assert "registro fue exitoso" in driver.page_source

# Iniciar sesión
driver.get("file:///C:/Users/jergarcia/Downloads/proyectoFinal_prog3/proyecto_final_prog3/index.html")
take_screenshot("3_pagina_login")

email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys("registro_prueba@gmail.com.do")
password_input.send_keys("A*12345678")

login_button = driver.find_element(By.ID, "login_button")
login_button.click()
take_screenshot("4_login_completado")

# Verificar inicio de sesión exitoso
assert "inicio de sesión fue exitoso" in driver.page_source

# Cerrar sesión
logout_button = driver.find_element(By.ID, "logout_button")
logout_button.click()
take_screenshot("5_logout_completado")

# Verificar cierre de sesión
assert "Sesión cerrada correctamente" in driver.page_source

# Cerrar el navegador
driver.quit()
