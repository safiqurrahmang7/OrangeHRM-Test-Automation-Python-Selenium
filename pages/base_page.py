import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    MODULE = (By.CSS_SELECTOR,'.oxd-main-menu-item.active')
    def find_element(self, locator_type, locator_value):
        """Finds a web element."""
        return self.driver.find_element(locator_type, locator_value)

    def wait_for_element(self, locator_type, locator_value, timeout=10):
        """Waits for an element to be visible."""
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator_value)))

    def is_element_displayed(self, locator_type, locator_value):
        """Checks if an element is displayed."""
        try:
            return self.find_element(locator_type, locator_value).is_displayed()
        except:
            return False

    @allure.step("get the active module")
    def get_active_module(self,module_name):

        return self.find_element(*self.MODULE).text


