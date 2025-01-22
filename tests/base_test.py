import pytest
from utils.browser import Browser
from utils.config import Config

@pytest.fixture(scope="function")
def driver():
    # Initialize the driver
    driver = Browser.get_driver(Config.BROWSER)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    yield driver
    # Quit the driver after the test
    driver.quit()
