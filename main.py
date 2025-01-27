from utils.config import Config
from utils.browser import Browser
from pages.base_page import BasePage
from resources.test_data import credentials


def main():
    # Initialize the WebDriver from Browser class
    driver = Browser.get_driver(Config.BROWSER)
    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)

    try:
        # Create an instance of BasePage
        base_page = BasePage(driver)

        # Run login tests using credentials from test_data.py
        for scenario, creds in credentials.items():
            print(f"Running test: {scenario}")
            base_page.login(creds["email"], creds["password"])
            print(f"Test completed for: {scenario}")

    except Exception as e:
        print(f"An error occurred during test execution: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
