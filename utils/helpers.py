import random
import string
import time
from datetime import datetime


def generate_random_email():
    """Generate a random email for testing"""
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "".join(random.choices(string.ascii_lowercase, k=7))
    return f"{username}@{domain}.com"


def generate_random_name():
    """Generate a random name for testing"""
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))


def generate_random_password():
    """Generate a random password for testing (8+ chars with at least one number and one special char)"""
    letters = "".join(random.choices(string.ascii_letters, k=6))
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_=+")

    # Combine and shuffle
    password = letters + digit + special
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)


def wait_for(condition_function, timeout=10, poll_frequency=0.5):
    """Wait for a condition to be true"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if condition_function():
            return True
        time.sleep(poll_frequency)
    return False


def get_current_timestamp():
    """Get current timestamp in a readable format"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def extract_number_from_text(text):
    """Extract a number from text"""
    return "".join(filter(str.isdigit, text))


def diff_count(before, after):
    """Calculate the difference between two counts"""
    try:
        return int(after) - int(before)
    except (ValueError, TypeError):
        return 0
