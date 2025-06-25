from .base_page import BasePage
from locators.locators import ProfilePageLocators
import allure
from config import PROFILE_URL


class ProfilePage(BasePage):
    """Profile page object"""

    url = PROFILE_URL

    def go_to_profile_section(self):
        """Go to profile section"""
        self.click_element(ProfilePageLocators.PROFILE_LINK)

    def go_to_order_history_section(self):
        """Go to order history section"""
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    def logout(self):
        with allure.step("Выход из личного кабинета"):
            self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def is_profile_form_visible(self):
        """Check if profile form is visible"""
        return self.is_element_visible(
            ProfilePageLocators.NAME_INPUT
        ) and self.is_element_visible(ProfilePageLocators.EMAIL_INPUT)

    def is_order_history_visible(self):
        with allure.step("Проверка, что отображается история заказов"):
            return self.is_visible(ProfilePageLocators.ORDER_HISTORY_BLOCK)

    def get_orders_count(self):
        """Get the number of orders in history"""
        orders = self.find_elements(ProfilePageLocators.ORDER_CARD)
        return len(orders)

    def click_on_order(self, index=0):
        """Click on order by index"""
        orders = self.find_elements(ProfilePageLocators.ORDER_CARD)
        if 0 <= index < len(orders):
            orders[index].click()
            return True
        return False

    def get_order_number(self, index=0):
        """Get order number by index"""
        orders = self.find_elements(ProfilePageLocators.ORDER_CARD)
        if 0 <= index < len(orders):
            number_element = orders[index].find_element(
                *ProfilePageLocators.ORDER_NUMBER_TEXT
            )
            # Clean up the text to get just the number
            return number_element.text.replace("#", "").strip()
        return None
