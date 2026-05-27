from selenium.webdriver.common.by import By


class authorizationPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def username(self, standard_user):
        self._driver.find_element(By.ID, "user-name").send_keys(
            standard_user)

    def password(self, secret_sauce):
        self._driver.find_element(By.ID, "password").send_keys(
            secret_sauce)

    def login_button(self):
        self._driver.find_element(
            By.ID, "login-button").click()
