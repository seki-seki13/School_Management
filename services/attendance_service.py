from models.attendance import Attendance
from database.connection import DatabaseConnection, transaction

class AttendanceService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_attendance(self, cursor, conn):
        cursor.callproc('v_attendance')
        attendance_records = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                att = Attendance(
                    attendance_id=None,
                    stud_id=None,
                    course_name=row['course_name'],
                    date_class=row['date_class'],
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    attendance_status=row['attendance_status'],
                    teacher_id=None
                )
                attendance_records.append(att)
        return attendance_records

    @transaction(dictionary=False)
    def add_attendance(self, cursor, conn, sch_id, s_id, status):
        new_record = (sch_id, s_id, status)
        cursor.callproc('add_attendance', new_record)