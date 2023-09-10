# Importar las librerías necesarias
# Asegúrate de haber instalado previamente 'selenium' usando 'pip install selenium'
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el controlador del navegador (en este caso, Chrome)
driver = webdriver.Chrome()

# Definir la URL a la que se desea acceder
url = 'https://www.nyse.com/index'

# Abrir la página web en el navegador
driver.get(url)

# Esperar hasta 5 segundos para que la página se cargue completamente
driver.implicitly_wait(5)

# Localizar el botón en la página web utilizando su XPath
boton = driver.find_element(By.XPATH, '//*[@id="integration-id-a30a997"]/div[2]/div/div/div[1]/div/button[2]')

# Hacer clic en el botón
boton.click()

# Esperar 2 segundos para que la página se actualice después de hacer clic en el botón
driver.implicitly_wait(2)

# Localizar el elemento que contiene la variación que se desea obtener
variacion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[10]/div[16]/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')

# Imprimir la variación de Bank of America Corporation en la consola
print("La variación de Bank of America Corporation:", variacion.text)

# Cerrar el navegador y liberar los recursos
driver.quit()
