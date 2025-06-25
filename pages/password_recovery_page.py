from .base_page import BasePage
from locators.locators import PasswordRecoveryPageLocators

import allure


class PasswordRecoveryPage(BasePage):
    """Password recovery page object"""

    def submit_recovery_email(self, email):
        """Submit email for password recovery"""
        self.send_keys_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY, email)
        self.click_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def go_to_login_page(self):
        """Navigate to login page"""
        self.click_element(PasswordRecoveryPageLocators.LOGIN_LINK)

    def is_recovery_form_displayed(self):
        """Check if recovery form is displayed"""
        return self.is_element_visible(
            PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY
        ) and self.is_element_visible(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def toggle_password_visibility(self):
        """Toggle password visibility (on reset password step)"""
        self.click_element(PasswordRecoveryPageLocators.PASSWORD_VISIBILITY_ICON)

    def is_password_field_active(self):
        """Check if password field is active/highlighted (on reset password step)"""
        # Check if password field exists first
        if not self.is_element_present(PasswordRecoveryPageLocators.PASSWORD_INPUT):
            return False

        password_field = self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT)
        # Check if the input has focus or active class
        return (
            password_field == self.driver.switch_to.active_element
            or "input_status_active" in password_field.get_attribute("class")
        )

    def enter_email(self, email):
        with allure.step(f"Ввод email: {email} в поле восстановления пароля"):
            self.send_keys_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY, email)

    def click_restore_button(self):
        with allure.step("Клик по кнопке 'Восстановить'"):
            self.click(PasswordRecoveryPageLocators.RESTORE_BUTTON)

    def password_field_type(self):
        with allure.step("Получение типа поля для ввода нового пароля"):
            input_password = self.wait_for_element_visible(
                PasswordRecoveryPageLocators.RESET_PASSWORD_INPUT
            )
            return input_password.get_attribute("type")
