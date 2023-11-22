def test_click_for_woman(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_for_woman()
    # Add assertions or verifications as needed
    excepted_title = 'Жіночий одяг від Harvest | Одяг українського бренду | Магазини: Київ, Львів, Дніпро і Харків'
    assert excepted_title == clothing_page.get_title()


def test_click_second_product(open_clothing_page):
    clothing_page = open_clothing_page
    clothing_page.click_second_product()
    # Add assertions or verifications as needed
    # For example, you can check if the product details are displayed
    assert clothing_page.is_product_details_displayed()
