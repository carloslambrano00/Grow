import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

df = pd.read_csv ('ListaSEM.csv')

print (df)

df['busqueda'] = df['GRUPO_EMPRESARIAL'] + ' Careers'

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver=webdriver.Chrome(options=options)

for index, row in df.iterrows():
    busqueda = row['busqueda']
    driver.get ('https://www.google.com/search?q=' + busqueda)
    
    try:
        portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/span/a')
        url_portal = portal.get_attribute('href')
    except NoSuchElementException:
        try:
            portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/span/a')
            url_portal = portal.get_attribute('href')
        except NoSuchElementException:
            try:
                portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/span/a')
                url_portal = portal.get_attribute('href')
            except NoSuchElementException:
                try:
                    portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/span/a')
                    url_portal = portal.get_attribute('href')
                except NoSuchElementException:
                    try:
                        portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div/div[1]/div/span/a')
                        url_portal = portal.get_attribute('href')
                    except NoSuchElementException:
                        try:
                            portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[2]/ul/li/div/div/div/div[1]/div/span/a')
                            url_portal = portal.get_attribute('href')
                        except NoSuchElementException:
                            try:
                                portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[2]/ul/li/div/div/div/div[1]/div/span/a')
                                url_portal = portal.get_attribute('href')
                            except NoSuchElementException:
                                try:
                                    portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/span/a')
                                    url_portal = portal.get_attribute('href')
                                except NoSuchElementException:
                                    try:
                                        portal = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
                                        url_portal = portal.get_attribute('href')
                                    except NoSuchElementException as e:
                                        url_portal = None
            
    time.sleep(4)
    
    if url_portal:
        df.at[index, 'url_Portal'] = '<a href = "' + url_portal + '">' + df.at[index,'GRUPO_EMPRESARIAL'] + '</a>'
        print ('La dirección es:', url_portal)
    else:
        print ('No existe URL')
        
driver.quit()

html=df.to_html (escape=False, columns=df.columns[0:])

with open ('Listas_Empresas_SEM_Portal.html', 'w') as f:
    f.write(html)
    
    
