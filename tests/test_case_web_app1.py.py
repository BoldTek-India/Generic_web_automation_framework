import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from resources.test_data import credentials
from pages.base_page import BasePage


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_invalid_password(driver):
    base_page = BasePage(driver)
    driver.get("https://dev-crm.boldtek.com/app/auth/login")  # Update with the actual URL

    # Login with invalid password
    base_page.login(credentials["invalid_password"]["email"], credentials["invalid_password"]["password"])

    # Verify error message
    error_message = base_page.get_error_message()
    assert error_message == "Incorrect password", f"Unexpected error message: {error_message}"
    print("Test Invalid Password: PASSED")


def test_unregistered_account(driver):
    base_page = BasePage(driver)
    driver.get("https://dev-crm.boldtek.com/app/auth/login")  # Update with the actual URL

    # Login with unregistered account
    base_page.login(credentials["unregistered_account"]["email"], credentials["unregistered_account"]["password"])

    # Verify error message
    error_message = base_page.get_error_message()
    assert error_message == "Your account is not registered", f"Unexpected error message: {error_message}"
    print("Test Unregistered Account: PASSED")


def test_valid_credentials(driver):
    base_page = BasePage(driver)
    driver.get("https://dev-crm.boldtek.com/app/auth/login")  # Update with the actual URL

    # Login with valid credentials
    base_page.login(credentials["valid_credentials"]["email"], credentials["valid_credentials"]["password"])

    # Verify login success
    assert base_page.is_logged_in() is True, "Login failed with valid credentials."
    print("Test Valid Credentials: PASSED")
