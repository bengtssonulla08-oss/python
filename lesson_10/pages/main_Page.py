import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class mainPage:

    def __init__(self, browser: WebDriver) -> None:
        self.driver: WebDriver = browser

    @allure.step("Добавляем рюкзак в корзину")
    def add_backpack(self) -> None:
        """Добавляем рюкзак в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    @allure.step("Добавляем футболку в корзину")
    def add_t_shirt(self) -> None:
        """Добавляем футболку в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    @allure.step("Добавляем комбинезон в корзину")
    def add_onesie(self) -> None:
        """Добавляем комбинезон в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переходим в корзину")
    def card_link(self) -> None:
        """Переходим на страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
