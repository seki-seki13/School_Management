import re
from datetime import datetime


def validate_input(prompt, pattern=None, error_msg="Invalid input."):
    while True:
        val = input(prompt).strip()
        if val.lower() == 'cancel': raise Exception('User canceled entry')
        if not val:
            print('[!] This field cannot be empty.')
            continue
        if pattern and not re.match(pattern, val):
            print(f'[!] {error_msg}')
            continue
        return val

def validate_number(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt).strip()
        if val.lower() == 'cancel':
            raise Exception('User canceled entry')
        try:
            num = int(val)
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
    print('\n[ Enter Details - Type "cancel" at any time to abort ]')

    try:
        f = validate_input('First Name: ')
        l = validate_input('Last Name: ')

        # Date Validation
        while True:
            d = input('DOB (YYYY-MM-DD): ').strip()
            try:
                datetime.strptime(d, '%Y-%m-%d')
                break
            except ValueError:
                print('[!] Invalid date format. Use YYYY-MM-DD.')

        t = validate_input('Town (Default Astana): ')
        a = validate_input('Address: ')

        # Phone Validation (Matching your SQL: +7 followed by 10 digits)
        p = validate_input('Phone (+7XXXXXXXXXX): ',
                           pattern=r'^\+7\d{10}$',
                           error_msg='Phone must start with '
                                     '+7 followed by 10 digits.')

        # Email Validation
        e = validate_input('Email: ',
                           pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',
                           error_msg='Invalid email format '
                                     '(e.g., name@domain.com).')

        return f, l, d, t, a, p, e

    except Exception as e:
        print(f'\nError: {e}')
        return None

def course_valid(prompt):
    while True:
        cid = validate_input(prompt,
                             pattern=r'^\d{3}[A-Z]{3}$',
                             error_msg='Invalid course ID (e.g., 001ALG).')
        return cid

def date_class_validator():
    while True:
        d = input('Date Class (yyyy-mm-dd): ').strip()
        try:
            datetime.strptime(d, '%Y-%m-%d')
            break
        except ValueError:
            print('[!] Invalid date format. Use YYYY-MM-DD.')
    return d

def grade_valid():
    while True:
        g_val = input('Final Grade (0-100): ').strip()
        try:
            g = float(g_val)
            if 0 <= g <= 100: break
            print('[!] Grade must be between 0 and 100.')
        except ValueError:
            print('[!] Please enter a valid decimal number.')
    return g