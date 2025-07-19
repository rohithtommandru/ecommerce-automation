from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.login_link = (By.LINK_TEXT, "Signup / Login")
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")

    def open_login_page(self):
        self.driver.find_element(*self.login_link).click()

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
