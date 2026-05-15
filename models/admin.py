# Import the parent class
from models.person import Person

class Administration(Person):
    """
    Represents administrative staff entities.
    Inherits from People class and stores its values in **kwargs.
    """
    def __init__(self, admin_id, pers_id, **kwargs):
        # Pass inherited attributes
        super().__init__(pers_id=pers_id, **kwargs)
        # Primary identifier
        self.__admin_id = admin_id

    # Allow safe and secure ID retrieval
    @property
    def admin_id(self):
        return self.__admin_id