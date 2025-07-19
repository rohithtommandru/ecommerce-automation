import time
from pages.product_page import ProductPage

def test_add_to_cart(driver):
    driver.get("https://automationexercise.com")
    product_page = ProductPage(driver)

    product_page.go_to_products_page()
    time.sleep(2)

    product_page.add_first_product_to_cart()
    product_page.view_cart_from_modal()

    assert product_page.is_product_in_cart(), "❌ Product was not added to the cart!"


