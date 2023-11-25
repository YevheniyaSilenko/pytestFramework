# https://store.ferrari.com/en-us/

# 30 XPATH locators
"""
1.loc_absolute=/html
2.loc_body=//body
3.loc_ferrari_logo=//img[@alt="Ferrari Logo"]
4.loc_main_nav=//nav[@class="main-nav"]
5.loc_shop_now_button=//button[contains(text(), "Shop Now")]
6.loc_featured_products_section=//section[h2[contains(text(), "Featured Products")]]
7.loc_new_arrivals_heading=//h2[contains(text(), "New Arrivals")]
8.loc_first_new_arrival_product=(//section[h2[contains(text(), "New Arrivals")]]//div[@class="product"])[1]
9.loc_shop_by_category=//section[h2[contains(text(), "Shop by Category")]
10.loc_clothing_category=//a[contains(text(), "Clothing")]
11.loc_accessories_category=//a[contains(text(), "Accessories")]'
12.loc_toys_and_models_category=//a[contains(text(), "Toys & Models")]
13.loc_search_input=//input[@id="search"]
14.loc_search_button=//button[@id="search-btn"]
15.loc_first_featured_product_title=(//section[h2[contains(text(), "Featured Products")]]//h3[@class="product-title"])[1]
16.loc_add_to_cart_button_first_featured_product=(//section[h2[contains(text(), "Featured Products")]]//div[@class="product"]//button[contains(text(), "Add to Cart")])[1]
17.loc_footer=//footer
18.loc_about_ferrari_footer=//footer//a[contains(text(), "About Ferrari")]
19.loc_contact_us_footer=//footer//a[contains(text(), "Contact Us")]
20.loc_privacy_policy_footer=//footer//a[contains(text(), "Privacy Policy")]
21.loc_follow_us_section_footer=//footer//section[h3[contains(text(), "Follow Us")]
22.loc_facebook_icon_footer=//footer//i[@class="fa fa-facebook"]
23.loc_twitter_icon_footer=//footer//i[@class="fa fa-twitter"]
24.loc_instagram_icon_footer=//footer//i[@class="fa fa-instagram"]
25.loc_newsletter_input=//input[@id="newsletter"]
26.loc_subscribe_button=//button[contains(text(), "Subscribe")]
27.loc_terms_of_use_footer=//footer//a[contains(text(), "Terms of Use")]
28.loc_faqs_footer=//footer//a[contains(text(), "FAQs")]
29.loc_privacy_policy_footer=//footer//a[contains(text(), "Privacy Policy")]
30.loc_find_a_store_footer=//footer//a[contains(text(), "Find a Store")]


###10CSS

1.XPath_locator: loc_absolute=/html
CSS_locator: css_absolute=html
2.XPath_locator: loc_ferrari_logo=//img[@alt="Ferrari Logo"]
CSS_locator: loc_shop_now_button=//button[contains(text(), "Shop Now")]
3.Path_locator: loc_shop_now_button=//button[contains(text(), "Shop Now")]
CSS_locator: css_shop_now_button=button:contains("Shop Now")
4.XPath_ocator: loc_clothing_category=//a[contains(text(), "Clothing")]
CSS_locator: css_clothing_category=a:contains("Clothing")
5.XPath_locator: loc_search_input=//input[@id="search"]
CSS_locator: css_search_input=input#search
6.XPath_locator: loc_add_to_cart_button_first_featured_product=(//section[h2[contains(text(), "Featured Products")]]//div[@class="product"]//button[contains(text(), "Add to Cart")])[1]
CSS_locator: css_add_to_cart_button_first_featured_product=section:has(h2:contains("Featured Products")) div.product button:contains("Add to Cart"):eq(0)
7.XPath_locator: loc_follow_us_section_footer=//footer//section[h3[contains(text(), "Follow Us")]
CSS_locator: css_follow_us_section_footer=footer section:has(h3:contains("Follow Us"))
8.XPath_locator: loc_subscribe_button=//button[contains(text(), "Subscribe")]
CSS_locator: css_subscribe_button=button:contains("Subscribe")
9.XPath_locator: loc_instagram_icon_footer=//footer//i[@class="fa fa-instagram"]
CSS_locator: css_instagram_icon_footer=footer i.fa.fa-instagram
10.XPath_locator: loc_find_a_store_footer=//footer//a[contains(text(), "Find a Store")]
CSS_locator: css_find_a_store_footer=footer a:contains("Find a Store")
"""