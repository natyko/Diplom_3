#

from .base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    """Login page object"""

    def go_to_register_page(self):
        """Navigate to registration page"""
        self.click_element(LoginPageLocators.REGISTER_LINK)

    def login(self, email, password):
        """Log in with provided credentials"""
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def go_to_forgot_password_page(self):
        """Navigate to forgot password page"""
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def toggle_password_visibility(self):
        """Toggle password visibility"""
        self.click_element(LoginPageLocators.PASSWORD_VISIBILITY_ICON)

    def is_password_field_active(self):
        """Check if password field is active (highlighted)"""
        password_field = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        # Check if the input has focus or active class
        return (
            password_field == self.driver.switch_to.active_element
            or "input_status_active" in password_field.get_attribute("class")
        )

    def login_with_valid_credentials(self, email=None, password=None):
        from config import TEST_USER
        from locators.locators import LoginPageLocators, MainPageLocators

        email = email or TEST_USER["email"]
        password = password or TEST_USER["password"]

        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

        self.wait_for_element_visible_by_locator(MainPageLocators.PROFILE_BUTTON)
