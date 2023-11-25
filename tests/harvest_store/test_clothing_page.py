def test_click_for_woman(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_woman()
    # Add assertions or verifications as needed
    excepted_title = 'Жіночий одяг від Harvest | Одяг українського бренду | Магазини: Київ, Львів, Дніпро і Харків'
    assert excepted_title == clothing_page.get_title()


def test_click_for_men(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_men()
    excepted_title = 'Чоловічий одяг від Harvest | Одяг українського бренду | Магазини: Київ, Львів, Дніпро і Харків'
    assert excepted_title == clothing_page.get_title()

def test_click_x_nu_ot(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_x_nu_ot()
    excepted_title = 'HARVEST X NU OT | Магазини: Київ, Львів, Дніпро і Харків'
    assert excepted_title == clothing_page.get_title()

def test_click_for_suits(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_suits()
    excepted_title = 'Купити стильний спортивний жіночий костюм - Одяг Harvest'
    assert excepted_title == clothing_page.get_title()


def test_click_for_shorts(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_shorts()
    excepted_title = 'Чоловічі шорти | Купити шорти чоловічі трикотажні | Harvest'
    assert excepted_title == clothing_page.get_title()

def test_click_for_sweetshorts(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_sweetshorts()
    excepted_title = 'Худі та світшоти для чоловіків від українського бренду - Harvest'
    assert excepted_title == clothing_page.get_title()

