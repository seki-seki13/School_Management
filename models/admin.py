from models.person import Person

class Administration(Person):
    def __init__(self, admin_id, **kwargs):
        super().__init__(**kwargs)
        self.__admin_id = admin_id

    @property
    def admin_id(self):
        return self.__admin_id