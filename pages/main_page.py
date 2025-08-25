from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()

    @allure.step("Click constructor button")
    def click_in_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Click place order button")
    def make_order(self):
        self.click_on_element(self.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step("Check if bun link is visible")
    def buns_link_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUNS_LINK)

    @allure.step("Click order feed link")
    def click_in_order_feed(self):
        self.click_on_element(self.main_page_locators.ORDER_FEED_LINK)

    @allure.step("Check if order feed header is visible")
    def order_feed_header_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Wait for order feed header to be visible")
    def wait_for_order_feed_header(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Click crater bun")
    def click_on_crater_bun(self):
        self.click_on_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Modal window close")
    def close_modal_window(self):
        self.click_on_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Wait for modal window to appear")
    def wait_for_modal_window(self):
        self.wait_visibility_of_element(
            self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
        )

    @allure.step("Wait for crater bun to be visible")
    def wait_for_bun(self):
        self.wait_visibility_of_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Modal window close button is visible")
    def close_modal_window_button_is_visible(self):
        return self.visibility_of_element(
            self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
        )

    @allure.step("Drag and drop bun to ingredients area")
    def drag_and_drop_bun(self):
        self.move_element(
            self.main_page_locators.CRATER_BUN,
            self.main_page_locators.BURGER_INGREDIENTS,
        )

    @allure.step("Check if bun counter is visible")
    def bun_counter_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUN_COUNTER)

    @allure.step("Check if place order button is visible")
    def place_order_button_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step("Wait for order number visibility")
    def wait_for_made_order_modal_window(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_ID)

    @allure.step("Order number is visible")
    def order_id_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_ID)
