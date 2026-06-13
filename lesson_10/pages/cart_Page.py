import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class cartPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver: WebDriver = browser

    @allure.step("Кликаем на кнопку")
    def click_checkout(self) -> None:
        """Кликает по кнопке."""
        self.driver.find_element(By.ID, "checkout").click()
