from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

firefox_options = Options()
firefox_options.add_argument("--ignore-ssl-errors=yes")
firefox_options.add_argument("--ignore-certificate-errors")
firefox_options.add_argument("--allow-running-insecure-content")

chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

class Browser:
    @staticmethod
    def get_driver(browser="chrome"):
        """Return a browser driver (Chrome or Firefox)."""
        if browser == "chrome":
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        return driver
