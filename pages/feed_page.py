from config import FEED_URL
from .base_page import BasePage
from locators.locators import FeedPageLocators, OrderDetailsPageLocators
from selenium.webdriver.common.by import By
import allure


class FeedPage(BasePage):
    url = FEED_URL

    def open_feed(self):
        """Open the feed page."""
        with allure.step("Opening the feed page"):
            self.open()

    def is_feed_loaded(self):
        """Check if the feed page is loaded."""
        with allure.step("Checking if the feed page is loaded"):
            # Use any element that exists on feed page
            return self.is_visible(FeedPageLocators.DONE_TOTAL)

    def click_order(self):
        with allure.step("Клик по первому заказу в списке"):
            self.click(FeedPageLocators.ORDER_CARD)

    def has_order_from_user(self, order_number):
        with allure.step(f"Проверка, что заказ с номером {order_number} есть в ленте"):
            xpath = FeedPageLocators.USER_ORDER.format(order_number)
            return self.is_visible((By.XPATH, xpath))

    def is_order_details_visible(self):
        """Check if the order details modal is visible."""
        with allure.step("Checking if the order details modal is visible"):
            return self.is_visible(OrderDetailsPageLocators.ORDER_NUMBER)

    def get_total_done(self):
        """Get the total number of completed orders."""
        with allure.step("Getting the total number of completed orders"):
            # Use base class method like working version
            return int(self.get_text(FeedPageLocators.DONE_TOTAL))

    def get_today_done(self):
        """Get the number of orders completed today."""
        with allure.step("Getting the number of orders completed today"):
            # Use base class method like working version
            return int(self.get_text(FeedPageLocators.DONE_TODAY))

    def is_order_in_progress(self, order_number):
        """Check if an order is in the 'In Progress' column."""
        with allure.step(f"Checking if order #{order_number} is in progress"):
            xpath = "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]".format(order_number)
            return self.is_visible((By.XPATH, xpath))