from models.course import Course
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class CoursesService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('course_id')
    @transaction(dictionary=True)
    def view_courses(self, cursor, conn):
        cursor.callproc('v_courses')
        courses = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                course = Course(
                    course_id=row['course_id'],
                    course_name=row['course_name']
                )
                courses.append(course)
        return courses

    @transaction(dictionary=False)
    def add_course(self, cursor, conn, c_id, c_name):
        new_course = (c_id, c_name)
        cursor.callproc('add_course', new_course)

    @transaction(dictionary=False)
    def update_course(self, cursor, conn, c_id, c_name):
        updated = (c_id, c_name)
        cursor.callproc('update_course', updated)

    @transaction(dictionary=False)
    def delete_course(self, cursor, conn, c_id):
        cursor.callproc('delete_course', (c_id,))