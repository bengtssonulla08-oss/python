from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get(" http://the-internet.herokuapp.com/login")
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text.strip())
sleep(3)
driver.quit()
