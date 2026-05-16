import re
from datetime import datetime

"""
An input validation Utility (R7).

Ensures data integrity and valid input at the application layer.
"""

def validate_input(prompt, pattern=None, error_msg="Invalid input."):
    """
    Generic function to validate string-based user input.
    :param prompt: The message displayed to the user.
    :param pattern: Optional regex pattern for strict format matching.
    :param error_msg: Feedback provided if the pattern match fails.
    :return: The validated string
    """
    while True:
        val = input(prompt).strip()
        # Allow user to abort the process,
        # raising an exception for the menu to catch
        if val.lower() == 'cancel': raise Exception('User canceled entry')

        # Ensure mandatory fields are not left empty
        if not val:
            print('[!] This field cannot be empty.')
            continue

        # Check against regex pattern if provided (e.g., Email or Phone)
        if pattern and not re.match(pattern, val):
            print(f'[!] {error_msg}')
            continue
        return val


def validate_number(prompt, min_val=None, max_val=None):
    """
    Function to validate numeric input and enforce range constraints.
    Implements try-except to handle non-integer values (R6).

    :param prompt: The message displayed to the user.
    :param min_val: The minimum acceptable integer value.
    :param max_val: The maximum acceptable integer value.
    :return: A validated integer.
    """
    while True:
        val = input(prompt).strip()
        if val.lower() == 'cancel':
            raise Exception('User canceled entry')
        try:
            num = int(val)
            # Range validation logic
            if min_val is not None and num < min_val:
                print(f'[!] Must be at least {min_val}.')
                continue
            if max_val is not None and num > max_val:
                print(f'[!] Cannot exceed {max_val}.')
                continue
            return num
        except ValueError:
            print('[!] Invalid input. Please enter a whole number.')


def get_pers_data():
    """
    Performs the collection of personal details for
    People-based entities.
    Ensures that names, dates, and contact info match
    SQL schema constraints.
    """
    print('\n[ Enter Details - Type "cancel" at any time to abort ]')

    try:
        f = validate_input('First Name: ')
        l = validate_input('Last Name: ')

        # Date of Birth validation using datetime library
        # for real-date verification
        while True:
            d = input('DOB (YYYY-MM-DD): ').strip()
            try:
                datetime.strptime(d, '%Y-%m-%d')
                break
            except ValueError:
                print('[!] Invalid date format. Use YYYY-MM-DD.')

        t = input('Town (Default Astana): ')
        if not t:
            t = 'Astana'
        a = validate_input('Address: ')

        # Phone Validation
        p = validate_input('Phone (+7XXXXXXXXXX): ',
                           pattern=r'^\+7\d{10}$',
                           error_msg='Phone must start with '
                                     '+7 followed by 10 digits.')

        # Email Validation
        e = validate_input('Email (name@domain.com): ',
                           pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',
                           error_msg='Invalid email format '
                                     '(e.g., name@domain.com).')

        return f, l, d, t, a, p, e

    except Exception as e:
        print(f'\nError: {e}')
        return None


def course_valid(prompt):
    """
    Validates Course IDs to ensure they match
    the meaningful key format.
    Example: 001ALG (3 digits followed by 3 uppercase letters).
    """
    while True:
        cid = validate_input(prompt,
                             pattern=r'^\d{3}[A-Z]{3}$',
                             error_msg='Invalid course ID (e.g., 001ALG).'
                             ).strip()
        return cid


def date_class_validator():
    """
    Ensures that class schedule dates are valid and follow the format.
    """
    while True:
        d = input('Date Class (yyyy-mm-dd): ').strip()
        try:
            datetime.strptime(d, '%Y-%m-%d')
            break
        except ValueError:
            print('[!] Invalid date format. Use YYYY-MM-DD.')
    return d


def grade_valid():
    """
    Enforces academic grade constraints (0.0 to 100.0).
    Implements float conversion with exception handling (R6).
    """
    while True:
        g_val = input('Final Grade (0-100): ').strip()
        if g_val.lower() == 'cancel': return None
        try:
            g = float(g_val)
            if 0 <= g <= 100:
                return g
            print('[!] Grade must be between 0 and 100.')
        except ValueError:
            print('[!] Please enter a valid decimal number.')