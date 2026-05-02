from models.person import Person

class Student(Person):
    def __init__(self, stud_id, **kwargs):
        super().__init__(**kwargs)
        self.__stud_id = stud_id

