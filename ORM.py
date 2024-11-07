import re

def validate_username(username):
    # Only allow alphanumeric characters and limited symbols
    if re.match("^[A-Za-z0-9_]+$", username):
        return True
    else:
        raise ValueError("Invalid username format")
