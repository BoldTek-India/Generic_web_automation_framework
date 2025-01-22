from config import Config
from web_app import WebApp

def main():
    # Specify the web app to test
    web_app_name = Config.WEB_APP_NAME

    # Initialize the WebApp instance
    app_instance = WebApp(web_app_name, Config)

    # Execute the test cases for the specified web app
    app_instance.run_tests()

if __name__ == "__main__":
    main()
