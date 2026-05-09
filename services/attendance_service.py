from models.attendance import Attendance
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class AttendanceService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('course_name')
    @transaction(dictionary=True)
    def view_attendance(self, cursor, conn):
        cursor.callproc('v_attendance')
        attendance_records = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                att = Attendance(
                    attendance_id=None,
                    schedule_id=None,
                    stud_id=None,
                    attendance_status=row['attendance_status'],
                    course_name=row['course_name'],
                    date_class=row['date_class'],
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    teacher_id=None
                )
                attendance_records.append(att)
        return attendance_records

    @sorted_by('date_class', reverse=True)
    @transaction(dictionary=True)
    def get_attendance_by_role(
            self, cursor, conn, role, pers_id, sch_id=None):
        attendance = []
        if role == 'Teacher':
            cursor.callproc('f_attendance_for_teacher',
                            (pers_id, sch_id))
            for result in cursor.stored_results():
                for row in result.fetchall():
                    att = Attendance(
                        attendance_id=None,
                        schedule_id=None,
                        stud_id=None,
                        attendance_status=row['attendance_status'],
                        course_name=row['course_name'],
                        date_class=row['date_class'],
                        student_first_name=row['student_first_name'],
                        student_last_name=row['student_last_name'],
                        teacher_id=None
                    )
                    attendance.append(att)

        else:
            cursor.callproc('f_attendance_for_student',
                            (pers_id,))
            for result in cursor.stored_results():
                for row in result.fetchall():
                    att = Attendance(
                        attendance_id=None,
                        schedule_id=None,
                        stud_id=None,
                        attendance_status=row['attendance_status'],
                        course_name=row['course_name'],
                        date_class=row['date_class'],
                        student_first_name=None,
                        student_last_name=None,
                        teacher_id=None
                    )
                    attendance.append(att)
        return attendance

    @transaction(dictionary=False)
    def add_attendance(self, cursor, conn, sch_id, s_id, status):
        new_record = (sch_id, s_id, status)
        cursor.callproc('add_attendance', new_record)