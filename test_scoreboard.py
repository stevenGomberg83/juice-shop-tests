import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper_methods import removeDismissButton


#GOAL is to successfully navigate to the OWASP Juice Shop's Hidden Score Board page

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



def test_scoreboard(driver):

    # Step 1: Navigate to the OWASP Juice Shop website first
    driver.delete_all_cookies()
    driver.get(BASE_URL)


    # Step 5: Verify that the session was cleared
    assert driver.current_url == BASE_URL, f"Expected {BASE_URL}, but got {driver.current_url}"
    print("Page loaded successfully after clearing storage.")


    #Wait up to 10 seconds for the website to load
    wait = WebDriverWait(driver, 10)
    time.sleep(1)

    #Remove Dismiss Notification for Cookies
    removeDismissButton(driver)
    print("Returned to Scoreboard Func")
    time.sleep(1)

    # Attempt to brute force to the hidden Score Board Page
    SCORE_BOARD_URL = BASE_URL + "/score-board"
    driver.get(SCORE_BOARD_URL)
    time.sleep(1)

    print("Going to attempt to identify Score Card")
    challenge_progress_score_card = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'hacking-challenge-progress-score-card'))
    )
    
    assert challenge_progress_score_card is not None, "Hacking Challenge Progress Score Card is not displayed"
    print("Hacking Challenge Progress Score Card found!")



