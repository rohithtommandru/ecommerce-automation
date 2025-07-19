from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://automationexercise.com/")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("rohithbaburohithbabu111@gmail.com", "Rohith@234")

    # Verify login success — you’ll need a real test account
    assert "Logged in as" in driver.page_source
