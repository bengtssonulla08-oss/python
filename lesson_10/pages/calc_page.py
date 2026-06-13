import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver: WebDriver = browser
        self.url: str = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self._delay_input: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self._result_field: tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открываем страницу калькулятора")
    def open(self) -> None:
        """Открываем страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Устанавливаем задержку.")
    def set_delay(self, time: str) -> None:
        """Устанавливаем задержку."""
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(time)

    @allure.step("Кликаем на кнопку.")
    def click_button(self, text: str) -> None:
        """Кликаем по кнопке."""
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Ожидаем результат.")
    def get_result(self, timeout: int) -> str:
        """Ожидаем появления результата и возвращает его."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._result_field, "15")
        )
        return self.driver.find_element(*self._result_field).text
