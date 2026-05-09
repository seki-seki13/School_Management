from models.teaching import Teaching
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class TeachingService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('last_name')
    @transaction(dictionary=True)
    def view_teaching_records(self, cursor, conn):
        cursor.callproc('v_teaching')
        teaching = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                teach = Teaching(
                    teach_course_id=row['teaching_ID'],
                    teacher_id=None,
                    course_id=None,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    course_name=row['course_name']
                )
                teaching.append(teach)
        return teaching

    @sorted_by('course_name')
    @transaction(dictionary=True)
    def get_my_courses(self, cursor, conn, pers_id):
        cursor.callproc('f_course_by_teacher', (pers_id,))
        courses = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                crs = Teaching(
                    teach_course_id=row['teaching_ID'],
                    teacher_id=None,
                    course_id=None,
                    course_name=row['course_name']
                )
                courses.append(crs)
        return courses

    @transaction(dictionary=False)
    def add_teaching(self, cursor, conn, t_id, c_id):
        new_teaching = (t_id, c_id)
        cursor.callproc('add_teaching', new_teaching)

    @transaction(dictionary=False)
    def update_teaching(self, cursor, conn, tch_id, t_id, c_id):
        updated = (tch_id, t_id, c_id)
        cursor.callproc('update_teaching', updated)

    @transaction(dictionary=False)
    def delete_teaching(self, cursor, conn, tc_id):
        cursor.callproc('delete_teaching', (tc_id,))