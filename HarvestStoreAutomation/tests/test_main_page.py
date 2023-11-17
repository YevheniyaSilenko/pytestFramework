import pytest
from HarvestStoreAutomation.page_objects.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainPage:

    def test_main_page_title(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        assert "Your Main Page Title" in main_page.get_title()

    def test_click_wishlist(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_wishlist()
        # Додайте перевірку для переходу на сторінку бажань

    def test_click_account(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_account()
        # Додайте перевірку для переходу на сторінку облікового запису

    def test_click_cart(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_cart()
        # Додайте перевірку для переходу на сторінку кошика

    def test_click_call(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_call()
        # Додайте перевірку для виклику

    def test_click_menu(self, setup):
        main_page = MainPage(setup)
        main_page.navigate_to_main_page()
        main_page.click_menu()
        # Додайте перевірку для відкриття меню
