from models.registration import Registration
from database.connection import DatabaseConnection, transaction

class RegistrationService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_registration(self, cursor, conn):
        cursor.callproc('v_registration')
        registration_records = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                reg = Registration(
                    reg_id=row['registration_ID'],
                    stud_id=None,
                    teach_course_id=None,
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    teacher_first_name=row['teacher_first_name'],
                    teacher_last_name=row['teacher_last_name'],
                    course_name=row['course_name'],
                    reg_date=row['date_registered']
                )
                registration_records.append(reg)
        return registration_records

    @transaction(dictionary=False)
    def add_registration(self, cursor, conn, s_id, tc_id):
        new_reg = (s_id, tc_id)
        cursor.callproc('add_registration', new_reg)

    @transaction(dictionary=False)
    def update_registration(self, cursor, conn, r_id, new_s_id, new_tc_id):
        updated = (r_id, new_s_id, new_tc_id)
        cursor.callproc('update_registration', updated)

    @transaction(dictionary=False)
    def delete_registration(self, cursor, conn, r_id):
        cursor.callproc('delete_registration', (r_id,))