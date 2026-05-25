from selenium.webdriver.common.by import By


class checkoutPage:
    def __init__(self, browser):
        self.driver = browser

    def form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total_element.text
