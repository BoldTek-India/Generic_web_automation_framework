import time
from resources.test_data import credentials, signup_data, test_files
from pages.crm_page import CRMBasePage
from tests.conftest import standalone_driver
import pyautogui

def test_01_signup(standalone_driver):
    crm_page = CRMBasePage(standalone_driver)
    print("Starting the signup process...")
    signup_message = crm_page.signup(signup_data["valid_details"])
    assert signup_message == "Successfully registered. Please check your registered mail.", f"Unexpected signup message: {signup_message}"
    print("Signup completed successfully!")

def test_invalid_phone_number_bug(standalone_driver):
    crm_page = CRMBasePage(standalone_driver)
    crm_page.signup(signup_data["invalid_phone"])
    success_message_element = crm_page.find_element("SignupPage", "Success Message")
    if success_message_element:
        success_message = success_message_element.text
        assert False, f"Bug Detected: Invalid phone number was accepted. Message: {success_message}"
    else:
        print("Test passed: Invalid phone number was rejected.")

def test_03_invalid_password(driver):
    crm_page = CRMBasePage(driver)
    error_message = crm_page.login(credentials["invalid_password"])
    assert error_message == "Invalid Password", f"Unexpected error message: {error_message}"
    crm_page.click_element("LoginPage", "Error Close Message")
    print("Test Invalid Password: PASSED")

def test_04_unregistered_account(driver):
    crm_page = CRMBasePage(driver)
    error_message = crm_page.login(credentials["unregistered_account"])
    assert error_message == "Your account is not registered!!!", f"Unexpected error message: {error_message}"
    crm_page.click_element("LoginPage", "Error Close Message")
    print("Test Unregistered Account: PASSED")

def test_05_valid_credentials(driver):
    crm_page = CRMBasePage(driver)
    crm_page.login(credentials["valid_credentials"])
    time.sleep(10)
    success_message = driver.title
    assert success_message == "Home", f"Unexpected success message: {success_message}"
    print("Test Valid Account: PASSED & redirected to the dashboard")

def test_06_import_leads(driver):
    crm_page = CRMBasePage(driver)
    crm_page.import_leads(test_files["import_leads_file"])