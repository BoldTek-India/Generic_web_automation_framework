import time
from resources.test_data import credentials
from resources.test_data import signup_data
from pages.base_page import BasePage
from tests.conftest import standalone_driver


# Signup with Valid credential
def test_01_signup(standalone_driver):
    base_page = BasePage(standalone_driver)

    # Step 1: Signup with valid details
    print("Starting the signup process...")

    base_page.click_element("SignupPage", "Signup Link")  # Navigate to the signup page
    base_page.send_keys("SignupPage", "Full Name Field", signup_data["valid_details"]["full_name"])
    base_page.send_keys("SignupPage", "Company Name Field", signup_data["valid_details"]["company_name"])
    base_page.send_keys("SignupPage", "Email Field", signup_data["valid_details"]["random_email"])
    base_page.send_keys("SignupPage", "Phone Number Field", signup_data["valid_details"]["phone_number"])
    base_page.click_element("SignupPage", "Terms Checkbox")
    base_page.scroll_to_element("SignupPage", "Signup Button")
    base_page.click_element("SignupPage", "Signup Button")
    time.sleep(5)
    signup_message = base_page.find_element("SignupPage", "Success Message").text
    assert signup_message == "Successfully registered. Please check your registered mail.", f"Unexpected signup message: {signup_message}"
    print("Signup completed successfully!")

#Signup with failed signup attempt
def test_invalid_phone_number_bug(standalone_driver):
# Test to verify that the system allows invalid phone numbers (e.g., 2 digits),which should not be allowed.
    base_page = BasePage(standalone_driver)

    # Step 1: Navigate to the Signup Page
    base_page.click_element("SignupPage", "Signup Link")

    # Step 2: Fill Signup Form with Invalid Phone Number (2 digits)
    base_page.send_keys("SignupPage", "Full Name Field", signup_data["invalid_phone"]["full_name"])
    base_page.send_keys("SignupPage", "Company Name Field", signup_data["invalid_phone"]["company_name"])
    base_page.send_keys("SignupPage", "Email Field", signup_data["invalid_phone"]["random_email"])
    base_page.send_keys("SignupPage", "Phone Number Field", signup_data["invalid_phone"]["phone_number"])
    base_page.click_element("SignupPage", "Terms Checkbox")

    # Step 3: Scroll to Submit Button and Click
    base_page.scroll_to_element("SignupPage", "Signup Button")
    base_page.click_element("SignupPage", "Signup Button")

    # Step 4: Verify Bug (Successful Submission Despite Invalid Phone Number)
    time.sleep(5)
    success_message_element = base_page.find_element("SignupPage", "Success Message")
    if success_message_element:
        success_message = success_message_element.text
        # If submission is successful, the test fails intentionally to demonstrate the bug
        assert False, f"Bug Detected: Invalid phone number was accepted. Message: {success_message}"
    else:
        # If the system rejects the invalid phone number, the test passes
        print("Test passed: Invalid phone number was rejected.")

# login part
def test_03_invalid_password(driver):
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

def test_04_unregistered_account(driver):
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

def test_05_valid_credentials(driver):
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