import allure
from pages.calc_page import CalcPage
from selenium import webdriver


class TestCalculator:
    @allure.severity("normal")
    @allure.feature("Сложение")
    @allure.title("Проверка сложения чисел с задержкой")
    @allure.description(
        "Тест устанавливает задержку 45 секунд, складывает 7 и 8 "
        "и проверяет результат."
    )
    def test_slow_calculator(self) -> None:
        browser = webdriver.Chrome()
        calc = CalcPage(browser)

        try:
            calc.open()
            calc.set_delay("45")
            calc.click_button("7")
            calc.click_button("+")
            calc.click_button("8")
            calc.click_button("=")
            result = calc.get_result(timeout=50)

            with allure.step("Проверяем, что сумма равна '15'"):
                assert result == "15"

        finally:
            browser.quit()
