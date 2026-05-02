from models.person import Person

class Teacher(Person):
    def __init__(self, teacher_id, **kwargs):
        super().__init__(**kwargs)
        self.__teacher_id = teacher_id

