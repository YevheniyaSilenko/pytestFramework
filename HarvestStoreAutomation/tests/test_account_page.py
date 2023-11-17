import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HarvestStoreAutomation.page_objects.login_page import LoginPage

@pytest.mark.usefixtures("setup")
def test_account_page_actions(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Виконаємо вхід на сторінку
    login_page.open("https://harvest-clothing.com.ua/login/")
    login_page.set_login("prencezza12@gmail.com")
    login_page.set_password("Canima_222")
    login_page.click_login_btn()

    # Перевіримо, чи ми на сторінці особистого кабінету
    assert "https://harvest-clothing.com.ua/account/" in driver.current_url

    # Задамо локатори для різних елементів на сторінці особистого кабінету
    edit_account_locator = (By.XPATH, '')
    change_password_locator = (By.XPATH, '')
    change_address_locator = (By.XPATH, '//*[@id="change-address"]')
    orders_locator = (By.XPATH, '//*[@id="orders"]')

    # Зачекаємо видимості різних елементів на сторінці
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(edit_account_locator))
    wait.until(EC.visibility_of_element_located(change_password_locator))
    wait.until(EC.visibility_of_element_located(change_address_locator))
    wait.until(EC.visibility_of_element_located(orders_locator))

    # Взаємодія з елементами
    driver.find_element(*edit_account_locator).click()
    # Тут ви можете додати перевірки або взаємодію зі сторінкою редагування облікового запису

    driver.find_element(*change_password_locator).click()
    # Тут ви можете додати перевірки або взаємодію зі сторінкою зміни пароля

    driver.find_element(*change_address_locator).click()
    # Тут ви можете додати перевірки або взаємодію зі сторінкою зміни адреси

    driver.find_element(*orders_locator).click()
    # Тут ви можете додати перевірки або взаємодію зі сторінкою замовлень

    # Додайте свої перевірки на кожному етапі, щоб підтвердити, що ви опинились на правильних сторінках або виконали відповідні дії
