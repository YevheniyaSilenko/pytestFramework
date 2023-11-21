import unittest
from selenium import webdriver
from main_page import MainPage
from HarvestStoreAutomation.page_objects.clothing_page import ClothingPage

class TestClothingPage(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_click_for_woman(self):
        main_page = MainPage(self.driver)
        main_page.navigate_to_main_page()

        clothing_page = ClothingPage(self.driver)
        clothing_page.click_first_product()

        # Add assertions or further actions based on the behavior you want to test
        # Example: self.assertTrue(some_condition)
        # You can check if the URL matches the expected URL or if specific elements are present on the page.

    def test_click_second_product(self):
        main_page = MainPage(self.driver)
        main_page.navigate_to_main_page()

        clothing_page = ClothingPage(self.driver)
        clothing_page.click_second_product()

        # Add assertions or further actions based on the behavior you want to test
        # Example: self.assertTrue(some_condition)
        # You can check if the URL matches the expected URL or if specific elements are present on the page.

if __name__ == "__main__":
    unittest.main()
