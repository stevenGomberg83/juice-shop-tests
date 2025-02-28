import os
import datetime
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Load the base URL from the environment; if not set, fall back to a default
BASE_URL = os.environ.get("JUICE_SHOP_URL")
LOGIN_EMAIL = "seleniumPractice@gmail.com"
LOGIN_PASSWORD = "badPassword123"

@pytest.fixture(scope="session")
def driver():
    # Configure Chrome to run in headless mode so tests can run without a UI
    options = Options()
    options.add_argument("--headless")
    # Initialize the Chrome WebDriver (ensure chromedriver is in your PATH)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_user_login(driver):
    # Clear all cookies to ensure a fresh session
    driver.delete_all_cookies()


    # Open a known website; here we use example.com for demonstration
    driver.get(BASE_URL)
    
    # Get the current time and print it to the console
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Test executed at:", current_time)


    #Wait up to 10 seconds for the website to load
    wait = WebDriverWait(driver, 10)


    # Step 0, remove the dismiss button warning
    dismiss_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Close Welcome Banner"]'))
    )
    assert dismiss_button is not None, "Dismiss button not found"
    print("Found dismiss button")
    dismiss_button.click()


    # Step 1: Identify the Account button
    account_button = wait.until(
        EC.element_to_be_clickable((By.ID, "navbarAccount"))
    )
    assert account_button is not None, "Account button not found"
    print("Found account button")
    # Optionally scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", account_button)

    account_button.click()
    print("Clicked account button")
    
    time.sleep(1)


    # Step 2: Identify the Login button
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "navbarLoginButton"))
    )
    assert login_button is not None, "Login button not found"
    print("Found login button")
    login_button.click()
    time.sleep(2)


    # Step 3: Find Email Field
    email_field = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    assert email_field is not None, "Email field not found"
    print("Found email field")
    email_field.send_keys(LOGIN_EMAIL)
    time.sleep(1)


    # Step 4: Find Password Field
    password_field = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    assert password_field is not None, "Password field not found"
    print("Found password field")
    password_field.send_keys(LOGIN_PASSWORD)
    time.sleep(1)

    # Step 5: Find Login Button
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )
    assert login_button is not None, "Login button not found"
    print("Found login button")
    login_button.click()
    time.sleep(3)

    show_cart_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Show the shopping cart"]'))
    )
    assert show_cart_button is not None, "Show cart button not found"
    print("Found show cart button")
    show_cart_button.click()
    time.sleep(3)











   


