from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.read_locators import get_locator_from_excel

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, page_name, element_name):
        locator_type, locator_value = get_locator_from_excel(page_name, element_name)
        if locator_type == "XPATH":
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator_value))
            )
        elif locator_type == "ID":
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, locator_value))
            )
        # Add other locator types as needed
        return None

    def click_element(self, page_name, element_name):
        element = self.find_element(page_name, element_name)
        if element:
            element.click()

    def send_keys(self, page_name, element_name, value):
        element = self.find_element(page_name, element_name)
        if element:
            element.send_keys(value)

    def login(self, email, password):
        # Perform login using locators from Excel
        self.send_keys("LoginPage", "Username Field", email)
        self.send_keys("LoginPage", "Password Field", password)
        self.click_element("LoginPage", "Login Button")

    def get_error_message(self):
        # Retrieve error message from the login page
        element = self.find_element("LoginPage", "Error Message")
        return element.text if element else None

    def is_logged_in(self):
        # Check if the user is logged in by verifying the page title
        return "Dashboard" in self.driver.title
