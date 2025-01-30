from utils.config import Config
from utils.browser import Browser
from pages.base_page import BasePage
from pages.web_app import WebApp

def main():

    # Specify the web app to test
    web_app_name = Config.WEB_APP_NAME  # Fetch the web app name from config

    # Initialize the WebApp instance
    app_instance = WebApp(web_app_name, Config)

    # Execute the test cases for the specified web app
    app_instance.run_tests()

if __name__ == "__main__":
    main()
