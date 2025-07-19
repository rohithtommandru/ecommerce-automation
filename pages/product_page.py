from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_link = (By.XPATH, "//a[@href='/products']")
        self.first_add_button = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")
        self.modal_view_cart_button = (By.XPATH, "//div[@id='cartModal']//a[@href='/view_cart']")
        self.cart_product = (By.XPATH, "//table[@id='cart_info_table']//tr")

    def go_to_products_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.products_link)
        ).click()

    def add_first_product_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable(self.first_add_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        time.sleep(1)
        add_button.click()

    def view_cart_from_modal(self):
        wait = WebDriverWait(self.driver, 10)
        view_cart = wait.until(EC.element_to_be_clickable(self.modal_view_cart_button))
        view_cart.click()

    def is_product_in_cart(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.cart_product)) is not None



