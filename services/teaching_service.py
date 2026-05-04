from models.teaching import Teaching
from database.connection import DatabaseConnection, transaction

class TeachingService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

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