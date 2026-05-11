from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("12345")
sleep(2)
input_field.clear()
sleep(2)
input_field.send_keys("54321")
sleep(2)
driver.quit()
