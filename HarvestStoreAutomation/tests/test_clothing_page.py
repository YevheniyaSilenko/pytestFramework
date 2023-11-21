import pytest
from selenium import webdriver
from HarvestStoreAutomation.page_objects.clothing_page import ClothingPage

class TestClothingPage:
    @pytest.fixture
    def setup(self):
        # Set up the WebDriver
        driver = webdriver.Chrome()
        yield driver
        # Teardown - close the WebDriver
        driver.quit()

    def test_click_for_woman(self, setup):
        clothing_page = ClothingPage(setup)
        clothing_page.navigate_to_clothing_page()
        clothing_page.click_for_woman()
        # Add assertions or verifications as needed
        assert 'Жінці' in clothing_page.get_title()

    def test_click_second_product(self, setup):
        clothing_page = ClothingPage(setup)
        clothing_page.navigate_to_clothing_page()
        clothing_page.click_second_product()
        # Add assertions or verifications as needed
        # For example, you can check if the product details are displayed
        assert clothing_page.is_product_details_displayed()
