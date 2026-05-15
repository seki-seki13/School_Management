# Importing database elements and decorators
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

# Importing CourseReport model for OOP consistency
from models.course import CourseReport


class ReportingUtils:
    """
    Utility class dedicated to generating analytical reports.
    It bridges the gap between SQL aggregate functions and the Python
    Object-Oriented model.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()


    # Sorting the loaded data by descending student count (R5)
    @sorted_by('total_students', reverse=True)
    @transaction(dictionary=True)
    def students_per_course(self, cursor, conn):
        """
        Generate a report on student enrollment numbers per course.
        Utilises the 'r_students_per_course' stored procedure.

        :return: A list of sorted CourseReport objects.
        """
        cursor.callproc('r_students_per_course')
        report = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Map rows to model
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    total_students=row['total_students']
                )
                report.append(rep)
        return report


    # Sorting the loaded data by descending average grade value (R5)
    @sorted_by('average_grade', reverse=True)
    @transaction(dictionary=True)
    def average_grade_per_course(self, cursor, conn):
        """
        Calculate the mean grade for every course in the system.
        Utilises the 'r_average_grade_per_course' stored procedure.

        :return: A list of sorted CourseReport objects.
        """
        cursor.callproc('r_average_grade_per_course')
        report = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Map rows to model
                rep = CourseReport(
                    course_id=None,
                    course_name=row['course_name'],
                    average_grade=row['average_grade']
                )
                report.append(rep)
        return report


    # Sorting the loaded data by descending attendance percentage (R5)
    @sorted_by('attendance_percentage', reverse=True)
    @transaction(dictionary=True)
    def attendance_summary(self, cursor, conn):
        """
        Generate statistics regarding student presence rates per course.
        Utilises the 'r_attendance_summary' stored procedure.

        :return: A list of sorted CourseReport objects.
        """
        cursor.callproc('r_attendance_summary')
        report = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Map rows to model
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