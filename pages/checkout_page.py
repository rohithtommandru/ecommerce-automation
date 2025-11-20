from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    cart_button = (By.XPATH, "//a[@href='/view_cart']")
    proceed_to_checkout = (By.XPATH, "//a[@class='btn btn-default check_out']")
    address_details = (By.XPATH, "//h2[text()='Address Details']")

    def go_to_cart(self):
        self.click(self.cart_button)

    def checkout(self):
        self.click(self.proceed_to_checkout)

    def is_checkout_page_displayed(self):
        return self.driver.find_element(*self.address_details).is_displayed()
