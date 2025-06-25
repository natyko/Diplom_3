import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class OrderAPI:
    """API client for order-related operations"""

    def __init__(self, auth_headers=None):
        self.base_url = os.getenv(
            "API_BASE_URL", "https://stellarburgers.nomoreparties.site/api"
        )
        self.headers = {"Content-Type": "application/json"}
        if auth_headers and "Authorization" in auth_headers:
            self.headers["Authorization"] = auth_headers["Authorization"]

    def get_ingredients(self):
        """Get all available ingredients"""
        endpoint = f"{self.base_url}/ingredients"
        response = requests.get(endpoint, headers=self.headers)
        return response

    def create_order(self, ingredients):
        """Create a new order with the given ingredient IDs"""
        endpoint = f"{self.base_url}/orders"
        payload = {"ingredients": ingredients}
        response = requests.post(
            endpoint, data=json.dumps(payload), headers=self.headers
        )
        return response

    def get_user_orders(self):
        """Get orders for the authenticated user"""
        endpoint = f"{self.base_url}/orders"
        response = requests.get(endpoint, headers=self.headers)
        return response

    def get_order_by_number(self, order_number):
        """Get order details by order number"""
        endpoint = f"{self.base_url}/orders/{order_number}"
        response = requests.get(endpoint, headers=self.headers)
        return response

    def get_all_orders(self):
        """Get all orders (feed)"""
        endpoint = f"{self.base_url}/orders/all"
        response = requests.get(endpoint, headers=self.headers)
        return response
