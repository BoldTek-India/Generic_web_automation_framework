import random
import string

def generate_random_email():
    """Generate a random email for the 'not registered' scenario."""
    domain = "@example.com"
    prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return prefix + domain

# Test data for login scenarios
credentials = {
    "invalid_password": {
        "email": "nitumoni@boldtek.com",
        "password": "WrongPassword123"
    },
    "unregistered_account": {
        "email": generate_random_email(),
        "password": "RandomPassword123"
    },
    "valid_credentials": {
        "email": "nitumoni@boldtek.com",
        "password": "Password@123"
    }
}
