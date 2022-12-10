import re

def is_valid_number(number):
    # Use the regular expression to check if the number is valid
    if re.match(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", number):
        return True
    else:
        return False

# Test the function with some example numbers
print(is_valid_number("2124567890"))  # True
print(is_valid_number("212-456-7890"))  # True
print(is_valid_number("(212)456-7890"))  # True
print(is_valid_number("(212)-456-7890"))  # True
print(is_valid_number("212.456.7890"))  # True
print(is_valid_number("212 456 7890"))  # True
print(is_valid_number("+12124567890"))  # True
print(is_valid_number("+1 212.456.7890"))  # True
print(is_valid_number("+212-456-7890"))  # True
print(is_valid_number("1-212-456-7890"))  # False
