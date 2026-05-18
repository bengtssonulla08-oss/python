from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
ajax_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@id="ajaxButton"]'))
    )
ajax_button.click()
green_banner = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
banner_text = green_banner.text
print(banner_text)
driver.quit()
