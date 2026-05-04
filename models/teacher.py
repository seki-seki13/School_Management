from models.person import Person

class Teacher(Person):
    def __init__(self, teacher_id, pers_id, **kwargs):
        super().__init__(pers_id=pers_id, **kwargs)
        self.__teacher_id = teacher_id

    @property
    def teacher_id(self):
        return self.__teacher_id