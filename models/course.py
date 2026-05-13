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
        return self.__course_name

class CourseReport(Course):
    def __init__(self, course_id, course_name, **kwargs):
        super().__init__(course_id=None, course_name=course_name)

        self.__total_students = kwargs.get('total_students')
        self.__average_grade = kwargs.get('average_grade')
        self.__total_records = kwargs.get('total_records')
        self.__present_count = kwargs.get('present_count')
        self.__attendance_percentage = kwargs.get('attendance_percentage')

    @property
    def total_students(self):
        return self.__total_students

    @property
    def average_grade(self):
        return self.__average_grade

    @property
    def total_records(self):
        return self.__total_records

    @property
    def present_count(self):
        return self.__present_count

    @property
    def attendance_percentage(self):
        return self.__attendance_percentage