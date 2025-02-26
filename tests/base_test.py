import pytest
import allure
from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage


class BaseTest:
    """Base test class for setup and teardown."""

    @pytest.fixture(scope="function", autouse=True)
    @allure.step("Setup WebDriver before test")
    def setup(self, request):
        """Setup WebDriver before each test and login."""
        self.driver = DriverFactory.get_driver()
        self.driver.get(ConfigReader.get_property("BASE_URL"))

        self.login = LoginPage(self.driver)
        self.login.sandbox()


        request.addfinalizer(self.teardown)

    @allure.step("tearDown WebDriver after each test")
    def teardown(self):
        """Teardown WebDriver after each test."""
        self.driver.quit()

