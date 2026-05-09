"""
Person Model - Represents a person in the system
Inherits validation from BaseModel (demonstrating inheritance and polymorphism)
"""

from models.trying_polymorp.base import BaseModel


class Person(BaseModel):
    """
    Base person class with validation.
    All people (students, teachers, admins) inherit from this.
    """

    def __init__(self, pers_id, f_name, l_name, dob, town, address, phone, email):
        """
        Initialize a person with validated data.

        Args:
            pers_id: Person ID from database
            f_name: First name
            l_name: Last name
            dob: Date of birth (YYYY-MM-DD format or date object)
            town: Town/city
            address: Address
            phone: Phone number (+7XXXXXXXXXX format)
            email: Email address
        """
        self.__pers_id = pers_id

        # Use validation methods from BaseModel (polymorphism in action)
        self.__f_name = self.validate_string(f_name, 'First name', min_length=3)
        self.__l_name = self.validate_string(l_name, 'Last name', min_length=3)
        self.__dob = self.validate_date(dob, 'Date of birth')
        self.__town = self.validate_string(town, 'Town', min_length=2)
        self.__address = self.validate_string(address, 'Address', min_length=3)
        self.__phone = self.validate_phone(phone)
        self.__email = self.validate_email(email)

    # Properties (read-only access)
    @property
    def pers_id(self):
        """Get person ID"""
        return self.__pers_id

    @property
    def first_name(self):
        """Get first name"""
        return self.__f_name

    @property
    def last_name(self):
        """Get last name"""
        return self.__l_name

    @property
    def dob(self):
        """Get date of birth"""
        return self.__dob

    @property
    def town(self):
        """Get town"""
        return self.__town

    @property
    def address(self):
        """Get address"""
        return self.__address

    @property
    def phone(self):
        """Get phone number"""
        return self.__phone

    @property
    def email(self):
        """Get email"""
        return self.__email