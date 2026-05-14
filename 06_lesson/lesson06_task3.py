from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "award"))
    )
third_image = driver.find_element(By.ID, "award")
image_src = third_image.get_attribute("src")
print(image_src)
driver.quit()
