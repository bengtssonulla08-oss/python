from selenium.webdriver.common.by import By


class cartPage:
    def __init__(self, browser):
        self.driver = browser

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
