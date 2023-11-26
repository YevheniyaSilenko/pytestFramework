
# Smoke Test: Verifies the behavior of clicking on the 'WOMAN' option
def test_click_for_woman(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_woman()
    # Add assertions or verifications as needed
    expected_title = 'Жіночий одяг від Harvest | Одяг українського бренду | Магазини: Київ, Львів, Дніпро і Харків'
    assert expected_title == clothing_page.get_title()

# Smoke Test: Verifies the behavior of clicking on the 'MEN' option
def test_click_for_men(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_men()
    expected_title = 'Чоловічий одяг від Harvest | Одяг українського бренду | Магазини: Київ, Львів, Дніпро і Харків'
    assert expected_title == clothing_page.get_title()

# Smoke Test: Verifies the behavior of clicking on the 'X NU OT' option
def test_click_x_nu_ot(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_x_nu_ot()
    expected_title = 'HARVEST X NU OT | Магазини: Київ, Львів, Дніпро і Харків'
    assert expected_title == clothing_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'SUITS' option
def test_click_for_suits(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_suits()
    expected_title = 'Купити стильний спортивний жіночий костюм - Одяг Harvest'
    assert expected_title == clothing_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'SHORTS' option
def test_click_for_shorts(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_shorts()
    expected_title = 'Чоловічі шорти | Купити шорти чоловічі трикотажні | Harvest'
    assert expected_title == clothing_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'SWEETSHORTS' option
def test_click_for_sweetshorts(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_sweetshorts()
    expected_title = 'Худі та світшоти для чоловіків від українського бренду - Harvest'
    assert expected_title == clothing_page.get_title()
