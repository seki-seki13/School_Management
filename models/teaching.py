class Teaching:
    """
    Class representing a teacher-to-course assignment.
    Encapsulates data and then safely retrieves through @property.
    Input validation is mostly done in database and input layers
    """
    def __init__(
            self, teach_course_id, teacher_id,
            course_id, **kwargs):
        # Primary identifier
        self.__teach_course_id = teach_course_id

        # FKs
        self.__teacher_id = teacher_id
        self.__course_id = course_id
        self.__pers_id = kwargs.get('pers_id', '')

        # Attributes for cleaner and meaningful display
        self.__teacher_name = (f"{kwargs.get('first_name', '')} "
                               f"{kwargs.get('last_name')}").strip()
        self.__course_name = kwargs.get('course_name', 'Unknown')


    # Allow safe and secure data retrieval
    @property
    def tc_id(self):
        return self.__teach_course_id

    @property
    def t_name(self):
        return self.__teacher_name

    @property
    def course_name(self):
        return self.__course_name

    @property
    def course_id(self):
        return self.__course_id

    @property
    def pers_id(self):
        return self.__pers_id