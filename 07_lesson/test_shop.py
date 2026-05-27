from selenium import webdriver
from pages.authorization_Page import authorizationPage
from pages.main_Page import mainPage
from pages.cart_Page import cartPage
from pages.checkout_Page import checkoutPage


def test_authorization():
    browser = webdriver.Firefox()
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
    checkout_page.get_total_price
    total_price = checkout_page.get_total_price()
    browser.quit()
    assert total_price == "Total: $58.29"
