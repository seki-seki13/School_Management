# Importing model, database elements and decorators
from models.grades import Grade
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class GradesService:
    """
    Service layer for managing grade records.
    Handles the execution of stored procedures related to the
    Grades table and maps results into the corresponding model.

    CRUD: viewing, adding and updating.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by student name (R5)
    @sorted_by('student_name')
    @transaction(dictionary=True)
    def view_grades(self, cursor, conn):
        """
        Execute 'v_grades' stored procedure to get all grades
        records for administrative management.
        """
        cursor.callproc('v_grades')
        grades = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
                gr = Grade(
                    grade_id=None,
                    reg_id=row['reg_id'],
                    course_id=row['course_id'],
                    final_grade=row['final_grade'],
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    course_name=row['course_name']
                )
                grades.append(gr)
        return grades


    # Getting grades records based on user's role and
    # sorting the loaded data by final_grade (R5)
    @sorted_by('final_grade', reverse=True)
    @transaction(dictionary=True)
    def get_grades_by_role(
            self, cursor, conn, role, pers_id, course_id=None):
        """
        Execute role-specific grades displaying.
        Stored procedures: 'f_grades_teacher' and 'f_grades_student'.
        Ensures accessibility matching the authority level.
        """
        grades = []
        # Role-based accessibility
        if role == 'Teacher':
            cursor.callproc('f_grades_teacher', (pers_id, course_id))

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
                    gr = Grade(
                        grade_id=None,
                        reg_id=row['reg_id'],
                        final_grade=row['final_grade'],
                        student_first_name=row['student_first_name'],
                        student_last_name=row['student_last_name'],
                        course_name=row['course_name'],
                        course_id=row['course_id']
                    )
                    grades.append(gr)


        else:
            cursor.callproc('f_grades_student', (pers_id,))

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
                    gr = Grade(
                        grade_id=None,
                        reg_id=None,
                        final_grade=row['final_grade'],
                        student_first_name=None,
                        student_last_name=None,
                        course_name=row['course_name'],
                        course_id=row['course_id']
                    )
                    grades.append(gr)
        return grades


    # Creating a new grade (R4)
    @transaction(dictionary=False)
    def add_grade(self, cursor, conn, r_id, f_gr):
        """
        Execute 'add_grade' stored procedure to add a new grade record.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_grade = (r_id, f_gr)
        cursor.callproc('add_grade', new_grade)


    # Updating a grade value (R4)
    @transaction(dictionary=False)
    def update_grade(self, cursor, conn, r_id, grade):
        """
        Execute 'update_grade' stored procedure to update
        an existing grade value.
        """
        # Collect parameters into a tuple for the stored procedure call
        updated = (r_id, grade)
        cursor.callproc('update_grade', updated)