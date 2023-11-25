def test_click_for_backpacks(open_accessories_page):
    accessories_page = open_accessories_page
    accessories_page.click_for_backpacks()
    # Add assertions or verifications as needed
    excepted_title = 'Купити рюкзак молодіжний'
    assert excepted_title == accessories_page.get_title()