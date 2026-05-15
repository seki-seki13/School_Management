# Import the parent class
from models.person import Person

class Teacher(Person):
    """
    Represents teacher entities.
    Inherits from People class and stores its values in **kwargs.
    """
    def __init__(self, teacher_id, pers_id, **kwargs):
        # Pass inherited attributes
        super().__init__(pers_id=pers_id, **kwargs)
        # Primary identifier
        self.__teacher_id = teacher_id

    # Allow safe and secure ID retrieval
    @property
    def teacher_id(self):
        return self.__teacher_id