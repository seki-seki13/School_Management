class Authentication:
    """
    Class for authentication objects.
    Encapsulates data and then safely retrieves through @property.
    Input validation is mostly done in database and input layers.
    """
    def __init__(
            self, auth_id, pers_id, username, password, role=None):
        # Primary identifier
        self.__auth_id=auth_id

        # FK and primary attributes
        self.__pers_id=pers_id

        if not username:
            raise ValueError('Username required')
        self.__username=username

        if not password:
            raise ValueError('Password required')
        self.__password=password

        # User role holder for authorization
        self.__role=role


    # Allow safe and secure data retrieval
    @property
    def pers_id(self):
        return self.__pers_id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def role(self):
        return self.__role