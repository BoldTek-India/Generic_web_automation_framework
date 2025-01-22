from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be present."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Click on an element."""
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        """Enter text into a field."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Get text of an element."""
        element = self.wait_for_element(locator)
        return element.text
