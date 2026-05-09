class Attendance:
    def __init__(self, attendance_id, schedule_id, stud_id, attendance_status, **kwargs):
        self.__attendance_id =attendance_id
        self.__schedule_id = schedule_id
        self.__stud_id = stud_id
        self.__status = attendance_status

        self.__course_name = kwargs.get('course_name', 'None')
        self.__date_class = kwargs.get('date_class', '')
        self.__student_name = (f"{kwargs.get('student_first_name', '')} "
                             f"{kwargs.get('student_last_name', '')}").strip()
        self.__teacher_id = kwargs.get('teacher_id', '')

    @property
    def attendance_id(self):
        return self.__attendance_id

    @property
    def schedule_id(self):
        return self.__schedule_id

    @property
    def stud_id(self):
        return self.__stud_id

    @property
    def attendance_status(self):
        return self.__status

    @property
    def course_name(self):
        return self.__course_name

    @property
    def date_class(self):
        return self.__date_class

    @property
    def student_name(self):
        return self.__student_name

    @property
    def teacher_id(self):
        return self.__teacher_id