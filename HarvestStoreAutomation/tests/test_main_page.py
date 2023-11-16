import pytest
from page_objects.main_page import MainPage

class TestMainPage:
    @pytest.fixture
    def setup(self, create_driver):
        main_page = MainPage(create_driver)
        return main_page

    def test_search_product(self, setup):
        setup.navigate_to()
        setup.search_product('Ferrari Jacket')
        assert 'Search Results' in setup.driver.title

    def test_navigate_to_cart(self, setup):
        setup.navigate_to()
        setup.navigate_to_cart()
        assert 'Shopping Cart' in setup.driver.title

    def test_check_cart_icon_displayed(self, setup):
        setup.navigate_to()
        assert setup.is_displayed(setup.loc_cart_icon)

    def test_view_featured_products(self, setup):
        setup.navigate_to()
        assert setup.view_featured_products()

    def test_select_product_category(self, setup):
        setup.navigate_to()
        setup.select_product_category()
        assert 'Men' in setup.driver.title
