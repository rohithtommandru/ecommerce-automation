from pages.search_page import SearchPage

def test_search_product(driver):
    driver.get("https://automationexercise.com")
    search_page = SearchPage(driver)

    search_page.search_product("dress")
    assert search_page.is_result_displayed(), "❌ Search results not displayed!"
