# Importing model, database elements and decorators
from models.attendance import Attendance
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class AttendanceService:
    """
    Service layer for managing attendance records.
    Handles the execution of stored procedures related to the
    Attendance table and maps results into the corresponding model.

    CRUD: viewing and adding.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the general attendance data by course name (R5)
    @sorted_by('course_name')
    @transaction(dictionary=True)
    def view_attendance(self, cursor, conn):
        """
        Execute 'v_attendance' stored procedure to get all attendance
        records for administrative management.
        """
        cursor.callproc('v_attendance')
        attendance_records = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
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


    # Getting attendance records based on user's role and
    # sorting the loaded data by date of the class (R5)
    @sorted_by('date_class', reverse=True)
    @transaction(dictionary=True)
    def get_attendance_by_role(
            self, cursor, conn, role, pers_id, sch_id=None):
        """
        Execute role-specific attendance displaying.
        Stored procedures: 'f_attendance_for_teacher' and
        'f_attendance_for_student'.
        Ensures accessibility matching the authority level.
        """
        attendance = []

        # Role-based accessibility
        if role == 'Teacher':
            cursor.callproc('f_attendance_for_teacher',
                            (pers_id, sch_id))

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
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

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
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


    # Creating a new attendance record (R3)
    @transaction(dictionary=False)
    def add_attendance(self, cursor, conn, sch_id, s_id, status):
        """
        Execute 'add_attendance' stored procedure to
        add a new attendance record.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_record = (sch_id, s_id, status)
        cursor.callproc('add_attendance', new_record)