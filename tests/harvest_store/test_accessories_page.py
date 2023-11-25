def test_click_for_backpacks(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_backpacks()
    # Add assertions or verifications as needed
    excepted_title = 'Купити рюкзак молодіжний в Україні - інтернет магазин Harvest'
    assert excepted_title == accessories_page.get_title()


def test_click_for_bags(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_bags()
    # Add assertions or verifications as needed
    excepted_title = 'Купити сумки українського виробника Harvest шкіряні та з еко-шкіри'
    assert excepted_title == accessories_page.get_title()

def test_click_for_other(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_other()
    # Add assertions or verifications as needed
    excepted_title = 'Портмоне та гаманці від українського виробника Harvest'
    assert excepted_title == accessories_page.get_title()

def test_click_for_collections(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_collections()
    # Add assertions or verifications as needed
    excepted_title = 'Колекції від українського виробника | HARVEST'
    assert excepted_title == accessories_page.get_title()

def test_click_for_vintage(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_vintage()
    # Add assertions or verifications as needed
    excepted_title = 'Колекція аксесуарів VINTAGE від Harvest'
    assert excepted_title == accessories_page.get_title()


def test_click_for_active(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_active()
    # Add assertions or verifications as needed
    excepted_title = 'Колекція аксесуарів ACTIVE від Harvest'
    assert excepted_title == accessories_page.get_title()


def test_click_for_shuttle(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_shuttle()
    # Add assertions or verifications as needed
    excepted_title = 'Колекція аксесуарів SHUTTLE від Harvest'
    assert excepted_title == accessories_page.get_title()


def test_click_for_classic(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_classic()
    # Add assertions or verifications as needed
    excepted_title = 'Колекція аксесуарів CLASSIC від Harvest'
    assert excepted_title == accessories_page.get_title()


