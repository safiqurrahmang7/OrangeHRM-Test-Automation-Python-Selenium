import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("enter the username")
    def enter_username(self,username):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)

    @allure.step("enter the password")
    def enter_password(self,password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    @allure.step("Click the Login button")
    def submit(self):
        self.find_element(*self.LOGIN_BUTTON).click()
    @allure.step("verify the error_message")
    def get_error_message(self):
        """Returns login error message."""
        return self.find_element(*self.ERROR_MESSAGE).text

    @allure.step("navigate to the base URL")
    def sandbox(self):
        url = ConfigReader.get_property("BASE_URL")
        self.driver.get(url)