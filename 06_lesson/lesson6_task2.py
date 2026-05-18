from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )
input_field.send_keys("SkyPro")
updating_button = driver.find_element(By.ID, "updatingButton")
updating_button.click()
WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
print(updating_button.text)
driver.quit()
