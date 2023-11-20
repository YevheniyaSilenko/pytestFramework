import pytest
from selenium import webdriver
from HarvestStoreAutomation.page_objects.main_page import MainPage


class TestMainPage:
    @pytest.fixture
    def setup(self):
        # Set up the WebDriver
        driver = webdriver.Chrome()
        yield driver
        # Teardown - close the WebDriver
        driver.quit()

    def test_main_page_title(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        assert "Harvest - рюкзаки та сумки від українського молодіжного бренду" in main_page.get_title()

    def test_click_wishlist(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_wishlist()
        assert "Мої закладки" in main_page.get_title()

    def test_click_account(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_account()

    def test_click_cart(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_cart()

    @pytest.mark.skip(reason="Test skipped intentionally.")
    def test_click_contacts(self, setup):
        pytest.skip("Skipping test_click_contacts")

    @pytest.mark.skip(reason="Test skipped intentionally.")
    def test_click_information(self, setup):
        pytest.skip("Skipping test_click_information")


if __name__ == "__main__":
    pytest.main()
