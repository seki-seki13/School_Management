class Grade:
    def __init__(self, grade_id, reg_id, final_grade, **kwargs):
        self.__grade_id = grade_id
        self.__reg_id = reg_id
        self.__final_grade = final_grade

        self.__student_name = (f"{kwargs.get('student_first_name', '')} "
                               f"{kwargs.get('student_last_name', '')}").strip()
        self.__course_name = kwargs.get('course_name', 'Unknown')

    @property
    def grade_id(self):
        return self.__grade_id

    @property
    def reg_id(self):
        return self.__reg_id

    @property
    def final_grade(self):
        return self.__final_grade

    @property
    def student_name(self):
        return self.__student_name

    @property
    def course_name(self):
        return self.__course_name