"""
Base Model Class - Contains common validation methods for all models
This class demonstrates polymorphism - all child classes inherit these validation methods
"""

from datetime import datetime, date


class BaseModel:
    """
    Base class providing common validation methods for all models.
    This demonstrates the OOP principle of inheritance and polymorphism.
    """

    @staticmethod
    def validate_string(value, field_name, min_length=1, max_length=None):
        """Validates that a string field meets requirements."""
        if not value or not isinstance(value, str):
            raise ValueError(f'{field_name} is required and must be a string')

        value = value.strip()

        if len(value) < min_length:
            raise ValueError(f'{field_name} must be at least {min_length} characters')

        if max_length and len(value) > max_length:
            raise ValueError(f'{field_name} cannot exceed {max_length} characters')

        return value

    @staticmethod
    def validate_email(email):
        """Validates email format."""
        if not email or not isinstance(email, str):
            raise ValueError('Email is required')

        email = email.strip().lower()

        if '@' not in email or '.' not in email:
            raise ValueError(f'Invalid email format: {email}')

        return email

    @staticmethod
    def validate_phone(phone):
        """Validates phone number format (+7XXXXXXXXXX)."""
        if not phone or not isinstance(phone, str):
            raise ValueError('Phone number is required')

        phone = phone.strip()

        if not phone.startswith('+7') or len(phone) != 12:
            raise ValueError(f'Phone must be +7 followed by 10 digits. Got: {phone}')

        if not phone[2:].isdigit():
            raise ValueError(f'Phone digits must be numeric: {phone}')

        return phone

    @staticmethod
    def validate_date(value, field_name='Date', min_date=None):
        """Validates date format and range."""
        if not value:
            raise ValueError(f'{field_name} is required')

        # If it's already a date object, use it
        if isinstance(value, date):
            date_obj = value
        # If it's a string, parse it
        elif isinstance(value, str):
            try:
                date_obj = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError(f'{field_name} must be in YYYY-MM-DD format. Got: {value}')
        else:
            raise ValueError(f'{field_name} must be a date or string')

        # Set default min_date to 1945-01-01 if not specified
        if min_date is None:
            min_date = date(1945, 1, 1)

        if date_obj < min_date:
            raise ValueError(f'{field_name} cannot be before {min_date}. Got: {date_obj}')

        return date_obj