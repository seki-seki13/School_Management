class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id

        if not course_name:
            raise ValueError('Course name required')
        self.__course_name = course_name

    @property
    def course_id(self):
        return self.__course_id

    @property
    def course_name(self):
        return self.__course_id