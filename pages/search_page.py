from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    search_input = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    search_results = (By.XPATH, "//div[@class='productinfo text-center']")

    def search_product(self, product_name):
        self.type(self.search_input, product_name)
        self.click(self.search_button)

    def is_result_displayed(self):
        return len(self.driver.find_elements(*self.search_results)) > 0
