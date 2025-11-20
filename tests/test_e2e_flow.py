from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

def test_end_to_end_flow(driver):
    driver.get("https://automationexercise.com")

    login_page = LoginPage(driver)
    search_page = SearchPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.open_login_page()
    login_page.login("rohithbaburohithbabu111@gmail.com", "Rohith@234")

    # Search
    search_page.search_product("dress")

    # Add to cart
    product_page.add_first_product_to_cart()
    product_page.view_cart_from_modal()

    # Checkout
    checkout_page.checkout()

    assert checkout_page.is_checkout_page_displayed(), "❌ E2E checkout failed!"
