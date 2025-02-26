import pytest
import allure
from tests.base_test import BaseTest


@allure.feature("Login Tests")
class TestLogin(BaseTest):

    @allure.story("Valid Login Test")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("username, password", [
        ("Admin", "admin123")])
    def test_valid_login(self,username,password):

        with allure.step("Login the application"):
            self.login.enter_username(username)
            self.login.enter_password(password)
            self.login.submit()
        with allure.step("verify the DashBoard module is active"):
            module_name = self.login.get_active_module("Dashboard")
            assert "Dashboard" in module_name, "Module mismatch!"
        

    @allure.story("Invalid Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password", [
        ("Admin", "wrongpass"),
        ("invalidUser", "admin123")
    ])
    def test_invalid_login(self, username, password):
        """Test login with invalid credentials."""
        with allure.step("Login the application"):
            self.login.enter_username(username)
            self.login.enter_password(password)
            self.login.submit()
        with allure.step("verify the DashBoard module is active"):
            error_message = self.login.get_error_message()
            assert "Invalid credentials" in error_message, "Error message mismatch!"
