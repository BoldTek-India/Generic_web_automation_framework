import time
from pages.base_page import BasePage


class CRMBasePage(BasePage):
    """
    CRM-specific reusable functions.
    """

    def signup(self, details):
        """Signup using provided details (dictionary)."""
        self.click_element("SignupPage", "Signup Link")
        self.send_keys("SignupPage", "Full Name Field", details["full_name"])
        self.send_keys("SignupPage", "Company Name Field", details["company_name"])
        self.send_keys("SignupPage", "Email Field", details["random_email"])
        self.send_keys("SignupPage", "Phone Number Field", details["phone_number"])
        self.click_element("SignupPage", "Terms Checkbox")
        self.scroll_to_element("SignupPage", "Signup Button")
        self.click_element("SignupPage", "Signup Button")

        time.sleep(5)
        return self.find_element("SignupPage", "Success Message").text

    def get_signup_message(self):
        """ Retrieve success message after signup. """
        return self.find_element("SignupPage", "Success Message").text

    def login(self, credentials):
        """Login using provided credentials (dictionary)."""
        self.send_keys("LoginPage", "Username Field", credentials["email"])
        self.send_keys("LoginPage", "Password Field", credentials["password"])
        self.click_element("LoginPage", "Login Button")

        # Retrieve the error message after login attempt
        error_message_element = self.find_element("LoginPage", "Error Message")
        return error_message_element.text if error_message_element else ""

    def get_error_message(self):
        """ Retrieve error message after failed login. """
        element = self.find_element("LoginPage", "Error Message")
        return element.text if element else None

    def close_error_message(self):
        """ Clicks on error message close button. """
        self.click_element("LoginPage", "Error Close Message")

    def navigate_to_leads(self):
        """ Navigate to the Leads tab. """
        self.click_element("DashboardPage", "Leads Tab")

    def import_leads(self, file_path):
        """ Import leads using the given file path. """
        import pyautogui
        self.click_element("DashboardPage", "Leads Tab")
        # time.sleep(4)
        self.click_element("LeadsPage", "Import Leads Button")
        self.click_element("ImportLeadsPage", "Browse Button")
        pyautogui.write(file_path)
        pyautogui.press('enter')
        self.click_element("ImportLeadsPage", "Next Button")
