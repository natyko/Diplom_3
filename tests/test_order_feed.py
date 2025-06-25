
import  allure
from pages.feed_page import FeedPage


@allure.feature("Order Feed")
class TestOrderFeed:

    @allure.title("Open order details from feed")
    @allure.description("Verify that clicking an order opens its details")
    def test_open_order_details_from_feed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_order()
        assert feed_page.is_order_details_visible()

    @allure.title("Total done counter increases")
    @allure.description("Ensure the all-time counter increases after new order")
    def test_total_done_counter_increases(self, driver, logged_in_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = feed_page.get_total_done()

        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_total_done()

        assert after > before, f"Expected total done counter to increase (before={before}, after={after})"

    @allure.title("Today done counter increases")
    @allure.description("Ensure today's completed order counter increases")
    def test_today_done_counter_increases(self, driver, logged_in_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = feed_page.get_today_done()

        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_today_done()

        assert after > before, f"Expected today done counter to increase (before={before}, after={after})"

    @allure.title("Order appears in progress column")
    @allure.description("Ensure new order shows up in the 'In Progress' column")
    # def test_new_order_appears_in_progress(self, driver, logged_in_user, create_order):
    #     feed_page = FeedPage(driver)
    #     feed_page.open()
    #     assert feed_page.is_order_in_progress(create_order), "Order not found in progress column"
    def test_new_order_appears_in_progress(self, driver, login_user, create_order):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_order_in_progress(create_order)

    @allure.title("User order appears in feed")
    @allure.description("Verify that a user's created order appears in the feed")
    @allure.description("Проверка, что созданный пользователем заказ появляется в ленте")
    # def test_user_orders_appear_in_feed(self, driver,  create_order):
    #     feed_page = FeedPage(driver)
    #     feed_page.open()
    #     assert feed_page.has_order_from_user(create_order)
    def test_user_orders_appear_in_feed(self, driver, login_user, create_order):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.has_order_from_user(create_order)
