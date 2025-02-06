import random
import string
import os


def generate_random_email():
    """Generate a random email for the 'not registered' or 'signup' scenarios."""
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

# Test data for signup scenarios
signup_data = {
    "valid_details": {
        "full_name": "Nitumoni Sarma",
        "company_name": "BoldTek Pvt. Ltd.",
        "random_email": generate_random_email(),  # Using random email generation
        "phone_number": "9876543210"
    },
    "invalid_phone": {
        "full_name": "Nitumoni Sarma",
        "company_name": "BoldTek Pvt. Ltd.",
        "random_email": generate_random_email(),  # Using a wrong email to validate a test case
        "phone_number": "123"
    }
}

test_files = {
    "import_leads_file": os.path.join("C:", "Lead_Data", "Lead_data.xlsx")
}

