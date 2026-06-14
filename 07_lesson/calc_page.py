from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, browser):
        self.driver = browser
        self.url = "https://bonigarcia.dev/" \
                   "selenium-webdriver-java/slow-calculator.html"
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_field = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, time):
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(time)

    def click_button(self, text):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, timeout: int):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._result_field, "15")
        )
        return self.driver.find_element(*self._result_field).text
