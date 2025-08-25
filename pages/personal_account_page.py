import allure

from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()
        self.personal_account_locators = PersonalAccountLocators()
        self.login_page_locators = LoginPageLocators()

    @allure.step("Click on Personal Account button on main page")
    def click_on_personal_account_button(self):
        self.click_on_element(self.main_page_locators.PROFILE_BUTTON)

    @allure.step("Logout button is visible")
    def in_personal_account_page(self):
        return self.visibility_of_element(
            self.personal_account_locators.SIGN_OUT_LINK_IN_PROFILE
        )

    @allure.step("Wait for logout button")
    def wait_for_log_out_button(self):
        self.wait_visibility_of_element(
            self.personal_account_locators.SIGN_OUT_LINK_IN_PROFILE
        )

    @allure.step("Click on Order History")
    def click_on_order_history_button(self):
        self.click_on_element(self.personal_account_locators.ORDER_HISTORY)

    @allure.step("Wait for order to appear")
    def wait_for_order_history_is_displayed(self):
        self.wait_visibility_of_element(self.personal_account_locators.ORDER)

    @allure.step("Order is visible")
    def order_history_is_displayed(self):
        return self.visibility_of_element(self.personal_account_locators.ORDER)

    @allure.step("Click on logout button")
    def click_log_out_button(self):
        self.click_on_element(self.personal_account_locators.SIGN_OUT_LINK_IN_PROFILE)

    @allure.step("Wait until Login button is visible")
    def wait_for_log_in_button_is_displayed(self):
        self.wait_visibility_of_element(self.login_page_locators.ENTER_BUTTON)

    def login_button_is_displayed(self):
        return self.visibility_of_element(self.login_page_locators.ENTER_BUTTON)
