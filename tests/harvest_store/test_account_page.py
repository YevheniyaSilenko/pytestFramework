# Regression Test: Verifies the behavior of editing the account
def test_edit_account(open_account_page):
    account_page = open_account_page
    # Verify that we are on the account page
    assert "https://harvest-clothing.com.ua/account/" in account_page.get_current_url()
    account_page.click_edit_account()
    assert "https://harvest-clothing.com.ua/edit-account/" in account_page.get_current_url()

# Regression Test: Verifies the behavior of changing the password
def test_change_password(open_account_page):
    account_page = open_account_page
    # Change Password
    account_page.click_change_password()
    assert "https://harvest-clothing.com.ua/change-password/" in account_page.get_current_url()

# Regression Test: Verifies the behavior of changing the address
def test_change_address(open_account_page):
    account_page = open_account_page
    # Change Address
    account_page.click_change_address()
    assert "https://harvest-clothing.com.ua/address-book/" in account_page.get_current_url()

# Regression Test: Verifies the behavior of accessing the orders
def test_orders(open_account_page):
    account_page = open_account_page
    # Orders
    account_page.click_orders()
    assert "https://harvest-clothing.com.ua/order-history/" in account_page.get_current_url()
