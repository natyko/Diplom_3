import allure

from pages.main_page import MainPage
from tests.conftest import driver_signed_in


@allure.feature("Main Page")
class TestMainPage:
    @allure.description("Navigate by clicking on 'Constructor'")
    def test_constructor_link(self, driver):
        with allure.step("Click constructor link and verify page loads"):
            constructor_link = MainPage(driver)
            constructor_link.click_in_constructor()
            assert constructor_link.buns_link_is_visible()

    @allure.description("Navigate by clicking on 'Order Feed'")
    def test_order_feed(self, driver):
        with allure.step("Navigate to order feed and verify page loads"):
            order_feed = MainPage(driver)
            order_feed.click_in_order_feed()
            order_feed.wait_for_order_feed_header()
            assert order_feed.order_feed_header_is_visible()

    @allure.description("Clicking on ingredient opens modal window with details")
    def test_modal_window_is_seen(self, driver):
        with allure.step("Click ingredient and verify modal opens"):
            modal_window = MainPage(driver)
            modal_window.click_in_constructor()
            modal_window.wait_for_bun()
            modal_window.click_on_crater_bun()
            modal_window.wait_for_modal_window()
            assert modal_window.close_modal_window_button_is_visible()

    @allure.description("Modal window closes by clicking the close button")
    def test_close_modal_window(self, driver):
        with allure.step("Open and close modal window"):
            modal_window = MainPage(driver)
            modal_window.click_in_constructor()
            modal_window.wait_for_bun()
            modal_window.click_on_crater_bun()
            modal_window.wait_for_modal_window()
            modal_window.close_modal_window()
            assert modal_window.buns_link_is_visible()

    @allure.description("Adding ingredient to order increases ingredient counter")
    def test_counter(self, driver):
        with allure.step("Add ingredient and verify counter increases"):
            counter = MainPage(driver)
            counter.click_in_constructor()
            counter.wait_for_bun()
            counter.drag_and_drop_bun()
            assert counter.bun_counter_is_visible()

    @allure.description("Logged in user can place an order")
    def test_make_order_success(self, driver_signed_in):
        with allure.step("Create order and verify success"):
            order = MainPage(driver_signed_in)
            order.wait_for_bun()
            order.drag_and_drop_bun()
            order.make_order()
            order.wait_for_made_order_modal_window()
            assert order.order_id_is_visible()
