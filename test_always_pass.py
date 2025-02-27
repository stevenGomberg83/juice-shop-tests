import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load the base URL from the environment; if not set, fall back to a default
BASE_URL = os.environ.get("JUICE_SHOP_URL")

@pytest.fixture(scope="session")
def driver():
    # Configure Chrome to run in headless mode so tests can run without a UI
    options = Options()
    options.add_argument("--headless")
    # Initialize the Chrome WebDriver (ensure chromedriver is in your PATH)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_always_pass(driver):
    # Clear all cookies to ensure a fresh session
    driver.delete_all_cookies()
    
    # Open a known website; here we use example.com for demonstration
    driver.get(BASE_URL)
    
    # Get the current time and print it to the console
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Test executed at:", current_time)

    wait = WebDriverWait(driver, 10)
    toolbars = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mat-toolbar-row"))
    )

    # Iterate over all toolbar elements and select the one that contains "OWASP Juice Shop"
    header_toolbar = None
    for toolbar in toolbars:
        if "OWASP Juice Shop" in toolbar.text:
            header_toolbar = toolbar
            break

    #Ensure we found the desired header element
    assert header_toolbar is not None, "Header toolbar not found"
    print("Found header toolbar with text containing: OWASP Juice Shop")


   


