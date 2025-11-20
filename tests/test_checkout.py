from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

def test_checkout_flow(driver):
    driver.get("https://automationexercise.com")

    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    product_page.go_to_products_page()
    product_page.add_first_product_to_cart()
    product_page.view_cart_from_modal()

    checkout_page.checkout()
    assert checkout_page.is_checkout_page_displayed(), "❌ Checkout page not shown!"
