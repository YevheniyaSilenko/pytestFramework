import pytest
from selenium import webdriver
from page_objects.new_arrivals_page import NewArrivalsPage

class TestNewArrivalsPage:
    @pytest.fixture
    def setup(self):
        # Set up the WebDriver
        driver = webdriver.Chrome()
        yield driver
        # Teardown - close the WebDriver
        driver.quit()

    def test_new_arrivals_page_title(self, setup):
        new_arrivals_page = NewArrivalsPage(setup)
        new_arrivals_page.navigate_to_new_arrivals_page()
        assert "Новинки українського бренду HARVEST" in new_arrivals_page.get_title()

    def test_click_sweetshot1(self, setup):
        new_arrivals_page = NewArrivalsPage(setup)
        new_arrivals_page.navigate_to_new_arrivals_page()
        new_arrivals_page.click_sweetshot1()
        # Add assertions or verifications as needed
        assert 'Cвітшот на флісі чорний "HOLIDAY" - HARVEST' in new_arrivals_page.get_title()

    def test_click_sweetshot2(self, setup):
        new_arrivals_page = NewArrivalsPage(setup)
        new_arrivals_page.navigate_to_new_arrivals_page()
        new_arrivals_page.click_sweetshot2()
        # Add assertions or verifications as needed
        assert 'Костюм "HOLIDAY" таш – HARVEST' in new_arrivals_page.get_title()

    def test_click_casper3(self, setup):
        new_arrivals_page = NewArrivalsPage(setup)
        new_arrivals_page.navigate_to_new_arrivals_page()
        new_arrivals_page.click_casper3()
        # Add assertions or verifications as needed
        assert 'Костюм "HOLIDAY" таш – HARVEST' in new_arrivals_page.get_title()

