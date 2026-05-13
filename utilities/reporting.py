from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by
from models.course import CourseReport



class ReportingUtils:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('total_students', reverse=True)
    @transaction(dictionary=True)
    def students_per_course(self, cursor, conn):

        cursor.callproc('r_students_per_course')
        report = []

        for result in cursor.stored_results():
            for row in result.fetchall():
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    total_students=row['total_students']
                )
                report.append(rep)
        return report

    @sorted_by('average_grade', reverse=True)
    @transaction(dictionary=True)
    def average_grade_per_course(self, cursor, conn):

        cursor.callproc('r_average_grade_per_course')
        report = []

        for result in cursor.stored_results():
            for row in result.fetchall():
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    average_grade=row['average_grade']
                )
                report.append(rep)
        return report

    @sorted_by('attendance_percentage', reverse=True)
    @transaction(dictionary=True)
    def attendance_summary(self, cursor, conn):

        cursor.callproc('r_attendance_summary')
        report = []

        for result in cursor.stored_results():
            for row in result.fetchall():
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    total_records=row['total_records'],
                    present_count=row['present_count'],
                    attendance_percentage=
                    row['attendance_percentage']
                )
                report.append(rep)
        return report