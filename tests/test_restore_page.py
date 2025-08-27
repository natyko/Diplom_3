from pages.restore_page import RestorePage
import allure


@allure.feature("Password Recovery")
class TestRestorePage:
    @allure.description("Restore button is visible after clicking restore link")
    def test_restore_button(self, driver):
        with allure.step("Navigate to restore page and verify restore button"):
            restore_button = RestorePage(driver)
            restore_button.click_on_restore_link()
            assert restore_button.restore_button_is_visible()

    @allure.description("Email submission shows password recovery form")
    def test_restore_button_click(self, driver):
        with allure.step("Submit email and verify password recovery form appears"):
            restore_button = RestorePage(driver)
            restore_button.click_on_restore_link()
            restore_button.fill_email_field()
            restore_button.click_on_restore_button()
            restore_button.wait_visibility_of_eye_button()
            assert restore_button.eye_button_is_visible()

    @allure.description("Password field becomes active when clicked")
    def test_field_is_active(self, driver):
        with allure.step("Navigate to password field and verify it becomes active"):
            restore_button = RestorePage(driver)
            restore_button.click_on_restore_link()
            restore_button.fill_email_field()
            restore_button.click_on_restore_button()
            restore_button.wait_visibility_of_eye_button()
            restore_button.click_password_field()
            assert restore_button.field_is_active()
