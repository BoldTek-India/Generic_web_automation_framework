import pytest
from utils.browser import Browser
from utils.config import Config

@pytest.fixture(scope="session")
def driver():
    """
    Fixture for shared WebDriver instance.
    This instance is used by normal test cases.
    """
    driver = Browser.get_driver(Config.BROWSER)
    driver.get(Config.BASE_URL)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    yield driver
    driver.quit()

@pytest.fixture
def standalone_driver():
    """
    Fixture for standalone WebDriver instances for optional test cases.
    Ensures a fresh instance is used for each optional test.
    """
    driver = Browser.get_driver(Config.BROWSER)
    driver.get(Config.BASE_URL)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    yield driver
    driver.quit()
