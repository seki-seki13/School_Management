class Person:
    def __init__(
            self, pers_id, f_name, l_name, dob, town, address, phone, email):
        self.__pers_id = pers_id

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

    @property
    def first_name(self):
        return self.__f_name

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