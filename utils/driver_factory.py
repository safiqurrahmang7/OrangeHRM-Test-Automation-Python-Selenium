from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config_reader import ConfigReader

class DriverFactory:
    @staticmethod
    def get_driver():
        browser = ConfigReader.get_property("BROWSER") or "chrome"

        if browser.lower() == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)
        elif browser.lower() == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(int(ConfigReader.get_property("IMPLICIT_WAIT") or 10))
        driver.maximize_window()
        return driver
