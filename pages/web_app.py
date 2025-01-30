from utils.browser import Browser
import importlib
import pytest
class WebApp:

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.driver = None

    # def initialize_driver(self):
    #     """Initialize the browser driver."""
    #     self.driver = Browser.get_driver(self.config.BROWSER)
    #     self.driver.get(self.config.BASE_URL)
    #     self.driver.implicitly_wait(self.config.IMPLICIT_WAIT)

    def run_tests(self):
        """Run test cases using pytest."""
        test_module_path = f"tests/test_case_{self.name}.py"
        pytest.main(["-s", test_module_path])
