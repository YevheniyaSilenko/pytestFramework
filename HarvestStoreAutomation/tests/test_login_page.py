import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HarvestStoreAutomation.page_objects.login_page import LoginPage


@pytest.mark.usefixtures("setup")
def test_login_page(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Ваші тестові дії та перевірки тут
    login_page.open("https://harvest-clothing.com.ua/login/")

    # Зачекайте, поки вікно для логіну стане видимим
    login_window_locator = (By.XPATH, '//*[@id="loginForm"]/div/form')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(login_window_locator))

    # Затемнення екрану часто затримує інтерактивність, тому може знадобитися додаткове очікування видимості для кнопки
    login_button_locator = (By.XPATH, '//*[@id="loginForm"]/div/form/button[1]')
    wait.until(EC.visibility_of_element_located(login_button_locator))

    # Тепер можна взаємодіяти з елементами всередині вікна
    login_page.set_login("prencezza12@gmail.com")


    # Зачекайте, поки поле для пароля стане видимим



    # Тепер можна взаємодіяти з елементами всередині парольного вікна
    password_button_locator = (By.XPATH, '//*[@id="loginForm"]/div/form/div[2]')
    wait.until(EC.visibility_of_element_located(password_button_locator))

    login_page.set_password("Canima_222")


    login_page.click_login_btn()

    # Приклад перевірки
    assert "https://harvest-clothing.com.ua/account/" in driver.current_url
