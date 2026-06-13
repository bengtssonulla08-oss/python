import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class authorizationPage:

    def __init__(self, driver: WebDriver) -> None:
        self._driver: WebDriver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Вводим логин")
    def username(self, standard_user: str) -> None:
        """Вводим логин пользователя в поле ввода."""
        self._driver.find_element(By.ID, "user-name").send_keys(standard_user)

    @allure.step("Вводим пароль")
    def password(self, secret_sauce: str) -> None:
        """Вводим пароль пользователя в поле ввода."""
        self._driver.find_element(By.ID, "password").send_keys(secret_sauce)

    @allure.step("Кликаем на кнопку")
    def login_button(self) -> None:
        """Кликаем по кнопке для отправки формы."""
        self._driver.find_element(By.ID, "login-button").click()
