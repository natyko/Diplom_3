from selenium.webdriver.common.by import By

from config import BASE_URL
from .base_page import BasePage
from locators.locators import MainPageLocators

import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver, base_url=BASE_URL):
        super().__init__(driver, base_url)
        self.locators = MainPageLocators

    def select_buns_tab(self):
        """Select buns tab"""
        self.click_element(MainPageLocators.BUNS_TAB)

    def select_sauces_tab(self):
        """Select sauces tab"""
        self.click_element(MainPageLocators.SAUCES_TAB)

    def select_fillings_tab(self):
        """Select fillings tab"""
        self.click_element(MainPageLocators.FILLINGS_TAB)

    def get_all_ingredients(self):
        """Get all ingredients on the current tab"""
        return self.find_elements(MainPageLocators.INGREDIENT)

    def click_on_ingredient(self, index=0):
        """Click on an ingredient by index"""
        ingredients = self.get_all_ingredients()
        if 0 <= index < len(ingredients):
            ingredients[index].click()
            return True
        return False

    def click_ingredient(self):
        with allure.step("Клик по ингредиенту"):
            self.click(MainPageLocators.INGREDIENT)

    def is_ingredient_modal_open(self):
        """Check if ingredient modal is open"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    def close_ingredient_modal(self):
        """Close ingredient modal"""
        with allure.step("Закрытие окна деталей ингредиента"):
            self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)

    def is_ingredient_details_closed(self):
        with allure.step("Проверка, что окно деталей ингредиента закрыто"):
            return self.is_closed(MainPageLocators.INGREDIENT_DETAILS)

    def drag_ingredient_to_constructor(self, ingredient_index=0):
        """Drag an ingredient to the constructor"""
        # Get source ingredient
        ingredients = self.get_all_ingredients()
        if 0 <= ingredient_index < len(ingredients):
            source_element = ingredients[ingredient_index]

            # Get target (constructor)
            target_element = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR)

            # Perform drag and drop using JavaScript
            # (Selenium's ActionChains drag_and_drop can be unreliable)
            script = """
            function createEvent(typeOfEvent) {
                var event = document.createEvent('CustomEvent');
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                };
                return event;
            }

            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent('on' + event.type, event);
                }
            }

            function simulateDragDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_START: 'dragstart',
                    DRAG_END: 'dragend',
                    DRAG: 'drag',
                    DROP: 'drop'
                };

                var dragStartEvent = createEvent(EVENT_TYPES.DRAG_START);
                dispatchEvent(sourceNode, dragStartEvent);

                var dropEvent = createEvent(EVENT_TYPES.DROP);
                dispatchEvent(destinationNode, dropEvent, dragStartEvent.dataTransfer);

                var dragEndEvent = createEvent(EVENT_TYPES.DRAG_END);
                dispatchEvent(sourceNode, dragEndEvent, dragStartEvent.dataTransfer);
            }

            simulateDragDrop(arguments[0], arguments[1]);
            """
            self.driver.execute_script(script, source_element, target_element)
            return True
        return False



    def add_ingredient_to_burger(self):
        with allure.step("Перетаскивание ингредиента в корзину"):
            self.drag_and_drop(
                MainPageLocators.INGREDIENT, MainPageLocators.BASKET_LIST
            )

    def is_ingredient_counter_incremented(self):
        with allure.step("Проверка, что счётчик ингредиента увеличился"):
            value = int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))
            print("Ingredient counter value:", value)
            return value > 0

    def place_order(self):
        """Place an order safely"""
        order_button = self.find_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        self.wait_until_clickable(MainPageLocators.PLACE_ORDER_BUTTON)
        order_button.click()

    def is_order_confirmation_visible(self):
        """Check if order confirmation is visible"""
        return self.is_element_visible(MainPageLocators.ORDER_CONFIRMATION_MODAL)

    def get_order_number(self):
        self.wait(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))
        return self.find_element(MainPageLocators.ORDER_NUMBER).text.strip()

    # def close_order_confirmation(self):
    #     """Close order confirmation modal"""
    #     if self.is_order_confirmation_visible():
    #         self.click_element(MainPageLocators.ORDER_CONFIRMATION_CLOSE)
    def close_order_confirmation(self):
        """Close order confirmation modal"""
        with allure.step("Closing order confirmation"):
            # Click overlay instead of close button
            overlay = self.driver.find_element(By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
            overlay.click()

    def click_constructor_button(self):
        with allure.step("Click button 'Конструктор'"):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
            )
            self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def is_constructor_visible(self):
        with allure.step("Проверка, что отображается раздел с булками конструктора"):
            return self.is_visible(MainPageLocators.BUNS_TAB)

    def click_order_feed_button(self):
        with allure.step("Клик по кнопке 'Лента заказов'"):
            self.click_element(MainPageLocators.FEED_BUTTON)

    def is_ingredient_details_visible(self):
        with allure.step("Проверка, что окно деталей ингредиента отображается"):
            return self.is_visible(MainPageLocators.INGREDIENT_DETAILS)

    def is_order_details_visible(self):
        with allure.step("Проверка, что окно деталей заказа отображается"):
            return self.is_visible(MainPageLocators.ORDER_DETAILS)

    def click_place_order_button(self):
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    def click_profile_button(self):
        with allure.step("Клик по кнопке 'Личный кабинет'"):
            self.click(MainPageLocators.PROFILE_BUTTON)

    def login_if_needed(self):
        """Checks if login is needed and performs login"""
        if "login" in self.driver.current_url:
            from pages.login_page import LoginPage

            login_page = LoginPage(self.driver, self.driver.current_url)
            login_page.login_with_valid_credentials()
            WebDriverWait(self.driver, 10).until(lambda d: "login" not in d.current_url)

    def wait_for_element_visible_by_locator(self, locator, timeout=10):
        """Wait until the given element is visible on the page"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
