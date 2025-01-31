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
        return None

    def click_element(self, page_name, element_name):
        element = self.find_element(page_name, element_name)
        if element:
            element.click()

    def send_keys(self, page_name, element_name, value):
        element = self.find_element(page_name, element_name)
        if element:
            element.clear()
            element.send_keys(value)

    def scroll_to_element(self, page_name, element_name):

        element = self.find_element(page_name, element_name)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
