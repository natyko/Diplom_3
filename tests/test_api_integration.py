"""
API Integration tests showcasing modern hybrid approach
"""

import allure
import pytest
from api.user_api import UserAPI
from api.order_api import OrderAPI


@allure.feature("API Integration")
class TestAPIIntegration:
    # Tests demonstrating API + UI hybrid approach

    @allure.description("User creation via API")
    def test_user_creation_api(self):
        with allure.step("Create new user via API"):
            user_api = UserAPI()
            user_data = user_api.generate_test_user()

            response = user_api.register_user(user_data)

            assert response.status_code == 200, f"User creation failed: {response.text}"
            data = response.json()
            assert data["success"] is True
            assert "user" in data
            assert data["user"]["email"] == user_data["email"]

    @allure.description("Get user information via API")
    def test_get_user_info_api(self, test_user_api):
        with allure.step("Get user information via API"):
            user_info_response = test_user_api["api_client"].get_user_info()
            assert user_info_response.status_code == 200

            user_data = user_info_response.json()
            assert user_data["success"] is True
            assert user_data["user"]["email"] == test_user_api["email"]

    @allure.description("Update user information via API")
    def test_update_user_info_api(self, test_user_api):
        with allure.step("Update user information via API"):
            updated_name = "Updated API Test User"
            update_response = test_user_api["api_client"].update_user_info(
                {"name": updated_name}
            )
            assert update_response.status_code == 200

        with allure.step("Verify user information was updated"):
            updated_info_response = test_user_api["api_client"].get_user_info()
            updated_data = updated_info_response.json()
            assert updated_data["user"]["name"] == updated_name

    @allure.description("Order creation via API")
    def test_order_creation_api(self, order_api_with_auth):
        with allure.step("Create order via API"):
            order_response = order_api_with_auth.create_test_order()

            assert order_response.status_code == 200, (
                f"Order creation failed with status {order_response.status_code}: {order_response.text}"
            )

            order_data = order_response.json()
            assert order_data["success"] is True
            assert "order" in order_data
            assert "number" in order_data["order"]
            assert order_data["order"]["number"] > 0

    @allure.description("Verify created order appears in user orders")
    def test_order_appears_in_user_orders(self, order_api_with_auth):
        with allure.step("Create order and verify it appears in user order list"):
            # Create order first
            order_response = order_api_with_auth.create_test_order()
            assert order_response.status_code == 200
            order_data = order_response.json()
            created_order_number = order_data["order"]["number"]

            # Verify it appears in user's orders
            user_orders_response = order_api_with_auth.get_user_orders()
            assert user_orders_response.status_code == 200

            user_orders_data = user_orders_response.json()
            assert user_orders_data["success"] is True
            assert len(user_orders_data["orders"]) > 0

            order_found = any(
                order["number"] == created_order_number 
                for order in user_orders_data["orders"]
            )
            assert order_found, (
                f"Created order {created_order_number} not found in user orders"
            )

    @allure.description("Ingredients availability check via API")
    def test_ingredients_api(self):
        # Test ingredients endpoint for data validation
        order_api = OrderAPI()  # No auth needed for ingredients

        response = order_api.get_ingredients()
        assert response.status_code == 200, (
            f"Ingredients request failed: {response.text}"
        )

        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert len(data["data"]) > 0

        # Verify test ingredients are available
        from config import TEST_DATA

        available_ingredient_ids = [ingredient["_id"] for ingredient in data["data"]]

        for test_ingredient_id in TEST_DATA["ingredient_ids"]:
            assert test_ingredient_id in available_ingredient_ids, (
                f"Test ingredient {test_ingredient_id} not available"
            )

        # Verify ingredient structure
        first_ingredient = data["data"][0]
        required_fields = [
            "_id",
            "name",
            "type",
            "proteins",
            "fat",
            "carbohydrates",
            "calories",
            "price",
        ]
        for field in required_fields:
            assert field in first_ingredient, f"Missing required field: {field}"

    @allure.description("Public orders feed check via API")
    def test_public_orders_feed_api(self):
        # Test public orders feed API endpoint
        order_api = OrderAPI()  # No auth needed for public feed

        response = order_api.get_all_orders()
        assert response.status_code == 200, (
            f"Public feed request failed: {response.text}"
        )

        data = response.json()
        assert data["success"] is True
        assert "orders" in data
        assert "total" in data
        assert "totalToday" in data

        # Verify we have some orders
        assert data["total"] > 0
        assert len(data["orders"]) > 0

        # Verify order structure in feed
        first_order = data["orders"][0]
        required_order_fields = [
            "_id",
            "ingredients",
            "status",
            "number",
            "createdAt",
            "updatedAt",
        ]
        for field in required_order_fields:
            assert field in first_order, f"Missing required order field: {field}"


@allure.feature("API Error Handling")
class TestAPIErrorHandling:
    # Test API error scenarios

    @allure.description("Unauthorized request to get user orders")
    def test_unauthorized_user_orders(self):
        # Test that getting user orders without auth fails properly
        order_api = OrderAPI()  # No auth token

        response = order_api.get_user_orders()
        assert response.status_code == 401, (
            f"Expected 401 for unauthorized user orders request, got {response.status_code}: {response.text}"
        )

    @allure.description("Invalid login credentials")
    def test_invalid_login(self):
        # Test login with invalid credentials
        user_api = UserAPI()

        response = user_api.login_user("invalid@email.com", "wrongpassword")
        assert response.status_code == 401, "Expected 401 for invalid login"
        assert not user_api.is_authenticated(), (
            "User should not be authenticated after invalid login"
        )
