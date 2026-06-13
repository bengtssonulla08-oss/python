import allure
from pages.authorization_Page import authorizationPage
from pages.cart_Page import cartPage
from pages.checkout_Page import checkoutPage
from pages.main_Page import mainPage
from selenium import webdriver


class TestOnlinestore:
    @allure.severity("critical")
    @allure.feature("Покупка товаров")
    @allure.title("Проверяем покупку")
    @allure.description(
        "Авторизируемся, добавляем 3 товара в корзину "
        "и проверяем финальную стоимость."
    )
    def test_authorization(self) -> None:
        browser = webdriver.Firefox()

        try:
            auth_page = authorizationPage(browser)
            auth_page.username("standard_user")
            auth_page.password("secret_sauce")
            auth_page.login_button()

            main_page = mainPage(browser)
            main_page.add_backpack()
            main_page.add_onesie()
            main_page.add_t_shirt()
            main_page.card_link()

            cart_page = cartPage(browser)
            cart_page.click_checkout()

            checkout_page = checkoutPage(browser)
            checkout_page.form("Елена", "Орлова", "429570")
            total_price = checkout_page.get_total_price()

            with allure.step("Проверяем, что итоговая сумма равна $58.29'"):
                assert total_price == "Total: $58.29"

        finally:
            browser.quit()
