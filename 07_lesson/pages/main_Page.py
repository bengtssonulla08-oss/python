from selenium.webdriver.common.by import By


class mainPage:

    def __init__(self, browser):
        self.driver = browser

    def add_backpack(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_t_shirt(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def card_link(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
