# Smoke Test: Verifies the behavior of clicking on the 'BACKPACKS' option
def test_click_for_backpacks(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_backpacks()
    expected_title = 'Купити рюкзак молодіжний в Україні - інтернет магазин Harvest'
    assert expected_title == accessories_page.get_title()

# Smoke Test: Verifies the behavior of clicking on the 'BAGS' option
def test_click_for_bags(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_bags()
    expected_title = 'Купити сумки українського виробника Harvest шкіряні та з еко-шкіри'
    assert expected_title == accessories_page.get_title()

# Smoke Test: Verifies the behavior of clicking on the 'OTHER' option
def test_click_for_other(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_other()
    expected_title = 'Портмоне та гаманці від українського виробника Harvest'
    assert expected_title == accessories_page.get_title()

# Smoke Test: Verifies the behavior of clicking on the 'COLLECTIONS' option
def test_click_for_collections(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_collections()
    expected_title = 'Колекції від українського виробника | HARVEST'
    assert expected_title == accessories_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'VINTAGE' option
def test_click_for_vintage(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_vintage()
    expected_title = 'Колекція аксесуарів VINTAGE від Harvest'
    assert expected_title == accessories_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'ACTIVE' option
def test_click_for_active(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_active()
    expected_title = 'Колекція аксесуарів ACTIVE від Harvest'
    assert expected_title == accessories_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'SHUTTLE' option
def test_click_for_shuttle(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_shuttle()
    expected_title = 'Колекція аксесуарів SHUTTLE від Harvest'
    assert expected_title == accessories_page.get_title()

# Regression Test: Verifies the behavior of clicking on the 'CLASSIC' option
def test_click_for_classic(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_classic()
    expected_title = 'Колекція аксесуарів CLASSIC від Harvest'
    assert expected_title == accessories_page.get_title()
