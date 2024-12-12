from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("http://sga.leiteviana.com:8080/")

nome_field = driver.find_element(By.NAME, "user")
senha_field = driver.find_element(By.NAME, "senha")
submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/button")

nome_field.send_keys("TestName")
senha_field.send_keys("Senh@12345")

time.sleep(3)
submit_button.click()
time.sleep(5)