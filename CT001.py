from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    driver.get("http://sga.leiteviana.com:8080/")
    
    cadastrar_button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[3]/a")
    cadastrar_button.click()
    
    email_field = driver.find_element(By.NAME, "email")
    nome_field = driver.find_element(By.NAME, "user")
    senha_field = driver.find_element(By.NAME, "senha")
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/button")
    
    email_field.send_keys("teste@gmail.com")
    nome_field.send_keys("TestName")
    senha_field.send_keys("Senh@12345")

    time.sleep(3)
    submit_button.click()
    time.sleep(5)
    
finally:
    driver.quit()
