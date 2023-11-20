from base_page import BasePage

class MenApparelPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://store.ferrari.com/en-us/men/apparel'
    # Додайте елементи та методи для сторінки чоловічого одягу за необхідності
