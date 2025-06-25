# """Tests for password recovery functionality."""

import allure
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from utils.helpers import generate_random_email
from config import LOGIN_URL, FORGOT_PASSWORD_URL


@allure.feature("Password Recovery")
class TestPasswordRecovery:

    @allure.title("Test navigation to password recovery page")
    @allure.description(
        "Test that user can navigate to password recovery page from login page"
    )
    def test_navigate_to_password_recovery(self, driver):
        # Arrange
        login_page = LoginPage(driver, LOGIN_URL)

        # Act
        login_page.open()
        login_page.go_to_forgot_password_page()

        # Assert
        assert (
            driver.current_url == FORGOT_PASSWORD_URL
        ), "Failed to navigate to password recovery page"

    @allure.title("Test password recovery form submission")
    @allure.description("Test that user can submit email for password recovery")
    def test_password_recovery_form_submission(self, driver):
        # Arrange
        recovery_page = PasswordRecoveryPage(driver, FORGOT_PASSWORD_URL)
        test_email = generate_random_email()

        # Act
        recovery_page.open()
        recovery_page.submit_recovery_email(test_email)
        assert (
            recovery_page.is_recovery_form_displayed()
        ), "Recovery form should still be displayed after submission"

