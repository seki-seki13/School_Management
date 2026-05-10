"""
Reporting Utility - Generates reports directly from database
Uses stored procedures: r_students_per_course,
r_average_grade_per_course, r_attendance_summary
Returns data only - no displaying
"""

from database.connection import DatabaseConnection
from utilities.decorators import transaction
from models.course import CourseReport


class ReportingUtils:
    """Utility class for generating reports"""

    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def students_per_course(self, cursor, conn):
        """
        Get count of students per course.
        Uses: r_students_per_course stored procedure

        Returns:
            Dictionary {course_name: total_students}
        """
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

    @transaction(dictionary=True)
    def average_grade_per_course(self, cursor, conn):
        """
        Get average grade per course.
        Uses: r_average_grade_per_course stored procedure

        Returns:
            Dictionary {course_name: average_grade}
        """
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

    @transaction(dictionary=True)
    def attendance_summary(self, cursor, conn):
        """
        Get attendance summary by course.
        Uses: r_attendance_summary stored procedure

        Returns:
            Dictionary with course attendance statistics
        """
        cursor.callproc('r_attendance_summary')
        report = []

        for result in cursor.stored_results():
            for row in result.fetchall():
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    total_records=row['total_records'],
                    attendance_percentage=
                    row['attendance_percentage']
                )
                report.append(rep)
        return report