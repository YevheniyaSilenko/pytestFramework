import pytest
from selenium import webdriver
from page_objects.main_page import MainPage

class TestMainPage:
    @pytest.fixture
    def setup(self):
        # Set up the WebDriver
        driver = webdriver.Chrome()
        yield driver
        # Teardown - close the WebDriver
        driver.quit()

    # Smoke Test: Verifies the main page title
    def test_main_page_title(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        assert "Harvest - рюкзаки та сумки від українського молодіжного бренду" in main_page.get_title()

    # Smoke Test: Verifies the behavior of clicking on the wishlist
    def test_click_wishlist(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_wishlist()
        assert "Мої закладки" in main_page.get_title()

    # Regression Test: Verifies the behavior of clicking on the account
    def test_click_account(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_account()

    # Regression Test: Verifies the behavior of clicking on the cart
    def test_click_cart(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_cart()
