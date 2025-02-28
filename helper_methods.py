# Helper Methods for other Python Tests
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


def removeDismissButton(driver):
    # Step 0, remove the dismiss button warning
    """Removes the dismiss button for cookie notifications."""
    wait = WebDriverWait(driver, 10)
    try:
        dismiss_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Close Welcome Banner"]'))
        )
        assert dismiss_button is not None, "Failed to find the Dismiss button"
        print("Found dismiss button, clicking it...")
        dismiss_button.click()
    except Exception as e:
        print("Dismiss button not found or could not be clicked:", str(e))

def returnToHomePage(driver):
    # First check if we are currently at the homepage
    if driver.current_url == BASE_URL:
        print("Driver is at the BASE_URL")
        return
    else:
        print(f"Driver is NOT at BASE_URL! Current URL: {driver.current_url}")
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        assert driver.current_url == BASE_URL, "Failed to return to the homepage"
        print("Returned to the homepage")


def userLogin(driver, LOGIN_EMAIL, LOGIN_PASSWORD):
    print("|Helper|userLogin| Method started. LOGIN_EMAIL: " + LOGIN_EMAIL + "LOGIN_PASSWORD: " + LOGIN_PASSWORD)

    #Wait up to 10 seconds for the website to load
    wait = WebDriverWait(driver, 10)

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
    print("Found show cart button, therefore we are logged in")


