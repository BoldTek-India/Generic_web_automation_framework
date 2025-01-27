import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from resources.test_data import credentials
from pages.base_page import BasePage


# @pytest.fixture(scope="module")
# def driver():
#     # Setup WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()


def test_invalid_password(driver):
    base_page = BasePage(driver)

    # Login with invalid password
    base_page.send_keys("LoginPage", "Username Field", credentials["invalid_password"]["email"])
    base_page.send_keys("LoginPage", "Password Field", credentials["invalid_password"]["password"])
    base_page.click_element("LoginPage", "Login Button")

    # Verify error message

    error_message_element = base_page.find_element("LoginPage", "Error Message")
    error_message = error_message_element.text if error_message_element else ""
    assert error_message == "Invalid Password", f"Unexpected error message: {error_message}"
    print("Test Invalid Password: PASSED")



# def test_unregistered_account(driver):
#     base_page = BasePage(driver)
#
#     # Login with unregistered account
#     base_page.send_keys("LoginPage", "Username Field", credentials["unregistered_account"]["email"])
#     base_page.send_keys("LoginPage", "Password Field", credentials["unregistered_account"]["password"])
#     base_page.click_element("LoginPage", "Login Button")
#
#     # Verify error message
#     error_message_element = base_page.find_element("LoginPage", "Error Message")
#     error_message = error_message_element.text if error_message_element else ""
#     assert error_message == "Your account is not registered", f"Unexpected error message: {error_message}"
#     print("Test Unregistered Account: PASSED")


# def test_valid_credentials(driver):
#     base_page = BasePage(driver)
#
#     # Login with valid credentials
#     base_page.send_keys("LoginPage", "Username Field", credentials["valid_credentials"]["email"])
#     base_page.send_keys("LoginPage", "Password Field", credentials["valid_credentials"]["password"])
#     base_page.click_element("LoginPage", "Login Button")
#
#
#     # Verify login success
#     return "Dashboard" in driver.title
#     assert base_page.is_logged_in() is True, "Login failed with valid credentials."
#     print("Test Valid Credentials: PASSED")
