import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from resources.test_data import credentials
from resources.test_data import signup_data
from pages.base_page import BasePage


# @pytest.fixture(scope="module")
# def driver():
#     # Setup WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()
# Sign up first

def test_01_signup_and_login(driver):
    base_page = BasePage(driver)

    # Step 1: Signup with valid details
    print("Starting the signup process...")

    base_page.click_element("SignupPage", "Signup Link")  # Navigate to the signup page
    base_page.send_keys("SignupPage", "Full Name Field", signup_data["valid_details"]["full_name"])
    base_page.send_keys("SignupPage", "Company Name Field", signup_data["valid_details"]["company_name"])
    base_page.send_keys("SignupPage", "Email Field", signup_data["valid_details"]["random_email"])
    base_page.send_keys("SignupPage", "Phone Number Field", signup_data["valid_details"]["phone_number"])
    base_page.click_element("SignupPage", "Terms Checkbox")
    base_page.click_element("SignupPage", "Signup Button")

    # Verify successful signup
    time.sleep(5)
    signup_message = base_page.find_element("SignupPage", "Success Message").text
    assert signup_message == "Signup successful!", f"Unexpected signup message: {signup_message}"
    print("Signup completed successfully!")


# login part
def test_02_invalid_password(driver):
    base_page = BasePage(driver)

    # Login with invalid password
    base_page.send_keys("LoginPage", "Username Field", credentials["invalid_password"]["email"])
    base_page.send_keys("LoginPage", "Password Field", credentials["invalid_password"]["password"])
    base_page.click_element("LoginPage", "Login Button")

    # Verify error message

    error_message_element = base_page.find_element("LoginPage", "Error Message")
    error_message = error_message_element.text if error_message_element else ""
    assert error_message == "Invalid Password", f"Unexpected error message: {error_message}"
    base_page.click_element(page_name="LoginPage", element_name="Error Close Message")
    print("Test Invalid Password: PASSED")

def test_unregistered_account(driver):
    base_page = BasePage(driver)

    # Login with unregistered account
    base_page.send_keys("LoginPage", "Username Field", credentials["unregistered_account"]["email"])
    base_page.send_keys("LoginPage", "Password Field", credentials["unregistered_account"]["password"])
    time.sleep(5)
    base_page.click_element("LoginPage", "Login Button")

    # Verify error message
    error_message_element = base_page.find_element("LoginPage", "Error Message")
    error_message = error_message_element.text if error_message_element else ""
    assert error_message == "Your account is not registered!!!", f"Unexpected error message: {error_message}"
    base_page.click_element(page_name="LoginPage", element_name="Error Close Message")
    print("Test Unregistered Account: PASSED")


def test_valid_credentials(driver):
    base_page = BasePage(driver)

    # Login with valid credentials
    base_page.send_keys("LoginPage", "Username Field", credentials["valid_credentials"]["email"])
    base_page.send_keys("LoginPage", "Password Field", credentials["valid_credentials"]["password"])
    time.sleep(5)
    base_page.click_element("LoginPage", "Login Button")

    # Verify login success message while it redirects to the dashboard
    time.sleep(10)
    success_message = driver.title
    assert success_message == "Home", f"Unexpected success message: {success_message}"
    print("Test Valid Account: PASSED & redirected to the dashboard")