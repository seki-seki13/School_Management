# Import the abstract parent class
from models.person import Person

class Administration(Person):
    """
    Represents administrative staff.
    Inherits all personal attributes from Person via super().__init__().
    Adds admin-specific identifier on top of inherited data.
    """
    def __init__(self, admin_id, pers_id, **kwargs):
        # super() calls Person.__init__() passing inherited arguments
        # **kwargs forwards all personal fields without listing them explicitly
        super().__init__(pers_id=pers_id, **kwargs)

        # Admin-specific private attribute — not part of Person
        self.__admin_id = admin_id

    # Read-only property exposes admin ID safely
    @property
    def admin_id(self):
        return self.__admin_id