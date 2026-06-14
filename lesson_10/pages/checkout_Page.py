import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class checkoutPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver: WebDriver = browser

    @allure.step("Заполняем форму своими данными: {first_name} {last_name},"
                 "индекс: {postal_code}")
    def form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняем свои данные при оформлении заказа."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получаем итоговую стоимость заказа")
    def get_total_price(self) -> str:
        """Возвращаем итоговую стоимость заказа текстом."""
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total_element.text
