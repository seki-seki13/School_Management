class Teaching:
    def __init__(self, teach_course_id, teacher_id, course_id, **kwargs):
        # primary attributes of the Teaching table
        self.__teach_course_id = teach_course_id
        self.__teacher_id = teacher_id
        self.__course_id = course_id

        # display attributes. later used in rich table display
        self.__teacher_name = (f"{kwargs.get('first_name', '')} "
                               f"{kwargs.get('last_name')}").strip()
        self.__course_name = kwargs.get('course_name', 'Unknown')

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