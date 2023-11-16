from base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://store.ferrari.com/US/Account/User/Profile'
    # Додайте елементи та методи для сторінки профілю за необхідності
