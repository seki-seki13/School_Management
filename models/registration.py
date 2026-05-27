class Registration:
    """
    Class for registration records.
    Maps the student-to-teaching junction into an object.
    Encapsulates data and then safely retrieves through @property.
    Input validation is mostly done in database and input layers
    """
    def __init__(self, reg_id, stud_id,
                 teach_course_id, reg_date, **kwargs):
        # Primary identifier
        self.__reg_id = reg_id

        # Primary attributes
        self.__stud_id = stud_id
        self.__teach_course_id = teach_course_id
        self.__reg_date = reg_date

        # Attributes for cleaner and meaningful display
        self.__st_name = (f"{kwargs.get('student_first_name', '')} "
                          f"{kwargs.get('student_last_name', '')}"
                          ).strip()
        self.__teacher_name = (f"{kwargs.get('teacher_first_name', '')} "
                               f"{kwargs.get('teacher_last_name', '')}"
                               ).strip()
        self.__course_name = kwargs.get('course_name', 'Unknown')
        self.__course_id = kwargs.get('course_id', '')
        self.__final_grade = kwargs.get('')


    # Allow safe and secure data retrieval
    @property
    def reg_id(self):
        return self.__reg_id

    @property
    def stud_id(self):
        return self.__stud_id

    @property
    def st_name(self):
        return self.__st_name

    @property
    def teacher_name(self):
        return self.__teacher_name

    @property
    def course_name(self):
        return self.__course_name

    @property
    def course_id(self):
        return self.__course_id

    @property
    def reg_date(self):
        return self.__reg_date