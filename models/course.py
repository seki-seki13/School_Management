class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id

        if not course_name:
            raise ValueError('Course name required')
        self.course_name = course_name
