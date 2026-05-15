# Import the parent class
from models.person import Person

class Student(Person):
    """
    Represents student entities.
    Inherits from People class and stores its values in **kwargs.
    """
    def __init__(self, stud_id, pers_id, **kwargs):
        # Pass inherited attributes
        super().__init__(pers_id=pers_id, **kwargs)
        # Primary identifier
        self.__stud_id = stud_id

    # Allow safe and secure ID retrieval
    @property
    def student_id(self):
        return self.__stud_id