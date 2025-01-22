from utils.browser import Browser
import importlib

class WebApp:

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.driver = None

    def initialize_driver(self):
        """Initialize the browser driver."""
        self.driver = Browser.get_driver(self.config.BROWSER)
        self.driver.get(self.config.BASE_URL)
        self.driver.implicitly_wait(self.config.IMPLICIT_WAIT)

    def run_tests(self):
        """Run test cases associated with this web app."""
        self.initialize_driver()
        try:
            test_module_name = f"tests.test_case_{self.name}"
            test_module = importlib.import_module(test_module_name)
            test_functions = [func for func in dir(test_module) if func.startswith("test")]
            for test_function in test_functions:
                test_case = getattr(test_module, test_function)
                test_case(self.driver)
        finally:
            self.driver.quit()
