from pages.restore_page import RestorePage
import allure


@allure.feature("Password Recovery")
class TestRestorePage:
    @allure.title(
        "Кнопка Восстановить видна после перехода по ссылке Восстановить пароль на странице авторизации"
    )
    def test_restore_button(self, driver):
        restore_button = RestorePage(driver)
        restore_button.click_on_restore_link()
        assert restore_button.restore_button_is_visible()

    @allure.title(
        "При вводе почты и нажатии Восстановить появляется форма восстановления пароля"
    )
    def test_restore_button_click(self, driver):
        restore_button = RestorePage(driver)
        restore_button.click_on_restore_link()
        restore_button.fill_email_field()
        restore_button.click_on_restore_button()
        restore_button.wait_visibility_of_eye_button()
        assert restore_button.eye_button_is_visible()

    @allure.title("Password field becomes active when clicked")
    def test_field_is_active(self, driver):
        restore_button = RestorePage(driver)
        restore_button.click_on_restore_link()
        restore_button.fill_email_field()
        restore_button.click_on_restore_button()
        restore_button.wait_visibility_of_eye_button()
        restore_button.click_password_field(),
        assert restore_button.field_is_active()
