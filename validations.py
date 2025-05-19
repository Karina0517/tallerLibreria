# Validates if the input is a digit and within the specified range
def validate_option(option, min_val, max_val):
    return option.isdigit() and min_val <= int(option) <= max_val

# Validates that the input contains only alphabetic characters and spaces
def validate_alpha(text):
    return text.replace(" ", "").isalpha()

# Validates that the input is a valid year between 1500 and the current year
def validate_year(year):
    if not year.isdigit():
        return False
    year = int(year)
    from datetime import date
    return 1500 <= year <= date.today().year

# Continuously prompts the user until the input passes the given validation function
def prompt_until_valid(prompt_msg, validation_func, error_msg):
    while True:
        value = input(prompt_msg).strip()
        if validation_func(value):
            return value
        print(error_msg)