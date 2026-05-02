class Authentication:
    def __init__(
            self, auth_id, pers_id, username, password, role=None):
        self.__auth_id=auth_id
        self.__pers_id=pers_id
        if not username:
            raise ValueError('Username required')
        self.__username=username
        if not password:
            raise ValueError('Password required')
        self.__password=password
        self.__role=role

    @property
    def person_id(self):
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