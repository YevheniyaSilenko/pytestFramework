import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HarvestStoreAutomation.page_objects.login_page import LoginPage

@pytest.mark.usefixtures("setup")
def test_account_page_actions(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Perform login action to reach the account page
    login_page.open("https://harvest-clothing.com.ua/login/")
    login_page.set_login("prencezza12@gmail.com")
    login_page.set_password("Canima_222")
    login_page.click_login_btn()

    # Verify that we are on the account page
    assert "https://harvest-clothing.com.ua/account/" in driver.current_url

    # Define locators for different elements on the account page
    edit_account_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/edit-account/"]')
    change_password_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/change-password/"]')
    change_address_locator = (By.XPATH, '//a[@href="https://harvest-clothing.com.ua/address-book/"]')
    orders_locator = (By.CSS_SELECTOR, 'a[href="https://harvest-clothing.com.ua/order-history/"]')

    # Wait for the visibility and clickability of different elements on the page
    wait = WebDriverWait(driver, 20)

    # Edit Account
    edit_account_element = wait.until(EC.element_to_be_clickable(edit_account_locator))
    edit_account_element.click()
    assert "https://harvest-clothing.com.ua/edit-account/" in driver.current_url
    # Perform actions specific to the edit account page if needed

    # Change Password
    change_password_element = wait.until(EC.element_to_be_clickable(change_password_locator))
    change_password_element.click()
    assert "https://harvest-clothing.com.ua/change-password/" in driver.current_url
    # Perform actions specific to the change password page if needed

    # Change Address
    change_address_element = wait.until(EC.element_to_be_clickable(change_address_locator))
    change_address_element.click()
    assert "https://harvest-clothing.com.ua/address-book/" in driver.current_url
    # Perform actions specific to the change address page if needed

    # Orders
    orders_element = wait.until(EC.element_to_be_clickable(orders_locator))
    orders_element.click()

    # Wait for the page to fully load
    WebDriverWait(driver, 20).until(lambda driver: "order-history" in driver.current_url)

    # Assert the URL
    assert "https://harvest-clothing.com.ua/order-history/" in driver.current_url
    # Perform actions specific to the orders page if needed



