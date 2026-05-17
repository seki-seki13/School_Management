from abc import ABC  # ABC = Abstract Base Class

class Person(ABC):
    """
    Abstract parent class for all people in the system.
    Cannot be instantiated directly — must be subclassed.
    Encapsulates all personal data behind private attributes.
    """
    def __init__(self, pers_id, f_name, l_name, dob,
                 town, address, phone, email):
        # Private attributes (name-mangled with __) enforce encapsulation
        # Cannot be accessed directly from outside the class
        self.__pers_id = pers_id

        # Validation at model level — extra reliability layer (R-C1)
        if not f_name:
            raise ValueError('First name required')
        self.__f_name = f_name
        if not l_name:
            raise ValueError('Last name required')
        self.__l_name = l_name

        self.__dob = dob
        self.__town = town
        self.__address = address
        self.__phone = phone
        self.__email = email

    # @property decorators expose private data as read-only
    # External code can read but never directly overwrite these values
    @property
    def pers_id(self):
        return self.__pers_id

    @property
    def first_name(self):
        return self.__f_name

    # ... remaining properties follow the same pattern

    @property
    def last_name(self):
        return self.__l_name

    @property
    def dob(self):
        return self.__dob

    @property
    def town(self):
        return self.__town

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email