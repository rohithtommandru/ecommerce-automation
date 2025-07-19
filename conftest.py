# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # optional
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # wait max 10 seconds for each element

    yield driver  # test runs here

    # Teardown
    driver.quit()
