import allure

from pages.personal_account_page import PersonalAccountPage

from tests.conftest import driver_signed_in


@allure.feature("Personal Account")
class TestPersonalAccount:
    @allure.description("Navigate by clicking on 'Personal Account'")
    def test_profile_is_opened_success(self, driver_signed_in):
        with allure.step("Open personal account and verify access"):
            profile_button = PersonalAccountPage(driver_signed_in)
            profile_button.click_on_personal_account_button()
            profile_button.wait_for_log_out_button()
            assert profile_button.in_personal_account_page()

    @allure.description("Navigate to 'Order History' section")
    def test_order_history_is_displayed(self, driver_signed_in):
        with allure.step("Navigate to order history and verify it displays"):
            order_history = PersonalAccountPage(driver_signed_in)
            order_history.click_on_personal_account_button()
            order_history.wait_for_log_out_button()
            order_history.click_on_order_history_button()
            order_history.wait_for_order_history_is_displayed()
            assert order_history.order_history_is_displayed()

    @allure.description("Logout from account")
    def test_log_out(self, driver_signed_in):
        with allure.step("Log out from account and verify login page appears"):
            log_out = PersonalAccountPage(driver_signed_in)
            log_out.click_on_personal_account_button()
            log_out.wait_for_log_out_button()
            log_out.click_log_out_button()
            log_out.wait_for_log_in_button_is_displayed()
            assert log_out.login_button_is_displayed()
