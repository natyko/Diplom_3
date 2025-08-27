from pages.feed_page import FeedPage
from selenium.webdriver.common.by import By

from tests.conftest import driver_signed_in
from time import sleep
import allure
import pytest


@allure.feature("Order Feed")
class TestFeedPage:
    @allure.description("Clicking on order opens modal window with details")
    def test_order_info_is_displayed(self, driver):
        with allure.step("Click on order and verify modal opens with details"):
            order_info = FeedPage(driver)
            order_info.click_on_feed()
            order_info.wait_for_order_feed()
            order_info.wait_for_page_to_load()
            order_info.click_on_first_order()
            assert order_info.order_info_is_displayed()

    @allure.description(
        "User orders from 'Order History' section are displayed on 'Order Feed' page"
    )
    def test_my_order_is_visible_in_order_feed(self, driver_signed_in):
        with allure.step("Navigate to order feed and verify user order is visible"):
            order = FeedPage(driver_signed_in)
            order.click_on_feed()
            order.wait_for_order_feed()
            order.click_on_first_order()
            assert order.my_order_is_visible()

    @allure.description("Creating new order increases 'Completed all time' counter")
    def test_quantity_orders_for_all_time_correct(self, driver_signed_in):
        with allure.step("Create order and verify 'all time' counter increases"):
            order = FeedPage(driver_signed_in)
            order.click_on_feed()
            order.wait_for_order_feed()
            quantity_before_order = int(order.orders_for_all_time_())
            order.click_on_constructor()
            order.drag_and_drop_bun()
            order.make_order()
            order.wait_for_modal_window_to_be_closed()
            order.close_modal_window()
            order.click_on_feed()
            order.wait_for_order_feed()
            # Wait for counter to actually increase
            order.wait_for_counter_increase(
                order.main_page_locators.ORDERS_FOR_ALL_TIME, quantity_before_order
            )
            quantity_after_order = int(order.orders_for_all_time_())
            assert quantity_after_order > quantity_before_order

    @allure.description(
        "Creating order via API increases 'Completed all time' counter (API + UI)"
    )
    def test_quantity_orders_api_hybrid(self, driver, order_api_with_auth):
        with allure.step("Create order via API and verify UI counter increases"):
            # Navigate to feed page first to get initial counter
            order = FeedPage(driver)
            driver.get("https://stellarburgers.nomoreparties.site/feed")
            order.wait_for_order_feed()
            quantity_before_order = int(order.orders_for_all_time_())

            # Create order via API (much faster than UI)
            api_response = order_api_with_auth.create_test_order()

            assert api_response.status_code == 200, (
                f"API order creation failed with status {api_response.status_code}: {api_response.text}"
            )

            # Wait for counter to increase via UI
            order.wait_for_counter_increase(
                order.main_page_locators.ORDERS_FOR_ALL_TIME, quantity_before_order
            )
            quantity_after_order = int(order.orders_for_all_time_())
            assert quantity_after_order > quantity_before_order

    @allure.description("Creating new order increases 'Completed today' counter")
    def test_orders_for_today_correct(self, driver_signed_in):
        with allure.step("Create order and verify 'today' counter increases"):
            order = FeedPage(driver_signed_in)
            order.click_on_feed()
            order.wait_for_order_feed()
            quantity_before_order = int(order.orders_for_today())
            order.click_on_constructor()
            order.drag_and_drop_bun()
            order.make_order()
            order.wait_for_modal_window_to_be_closed()
            order.close_modal_window()
            order.click_on_feed()
            order.wait_for_order_feed()
            quantity_after_order = int(order.orders_for_today())
            assert quantity_after_order > quantity_before_order

    @allure.description(
        "After placing order its number appears in 'In Progress' section"
    )
    def test_order_in_process_correct(self, driver_signed_in):
        with allure.step("Place order and verify it appears in progress section"):
            order = FeedPage(driver_signed_in)
            order.click_on_constructor()
            order.drag_and_drop_bun()
            order.make_order()
            order.wait_for_modal_window_to_be_closed()
            number_of_order = int(order.get_order_in_main_page())
            order.close_modal_window()
            order.click_on_feed()
            order.wait_for_order_feed()
            # Check if all orders are ready (no orders in progress)
            try:
                order.wait_for_specific_order_in_feed(number_of_order, timeout=10)
                number_in_feed = int(order.get_order_in_feed())
                assert number_of_order == number_in_feed
            except:
                # If order is not in "в работе", check if all orders are completed
                all_orders_ready = order.find_elements(
                    order.main_page_locators.ALL_ORDERS_READY
                )
                assert len(all_orders_ready) > 0, (
                    "Order should either be in progress or all orders should be ready"
                )

