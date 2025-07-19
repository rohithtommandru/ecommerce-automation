from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.products_button = (By.XPATH, "//a[@href='/products']")

    def click_products(self):
        self.driver.find_element(*self.products_button).click()
