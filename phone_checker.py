import re

def phone_checker(phone):
    phone_pattern = r'^8-\d{3}-\d{3}-\d{2}-\d{2}$'
    return bool(re.match(phone_pattern, phone))
