# Importing model, database elements and decorators
from models.teaching import Teaching
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class TeachingService:
    """
    Service layer for managing teacher-to-course records.
    Handles the execution of stored procedures related to the
    Teaching table and maps results into the corresponding model.

    CRUD: full CRUD (R4).
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by last name (R5)
    @sorted_by('last_name')
    @transaction(dictionary=True)
    def view_teaching_records(self, cursor, conn):
        """
        Execute 'v_teaching' stored procedure to get all teaching
        records for administrative management.
        """
        cursor.callproc('v_teaching')
        teaching = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
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


    # Getting courses records based on current teacher's session
    # and sorting the loaded data by course name (R5)
    @sorted_by('course_name')
    @transaction(dictionary=True)
    def get_my_courses(self, cursor, conn, pers_id):
        """
        Executes 'f_course_by_teacher' stored procedure to find courses
        taught by a specific teacher.
        """
        cursor.callproc('f_course_by_teacher', (pers_id,))
        courses = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
                crs = Teaching(
                    teach_course_id=row['teaching_ID'],
                    teacher_id=None,
                    course_id=row['course_id'],
                    course_name=row['course_name']
                )
                courses.append(crs)
        return courses


    # Creating a new teaching record (R4)
    @transaction(dictionary=False)
    def add_teaching(self, cursor, conn, t_id, c_id):
        """
        Execute 'add_teaching' stored procedure to add a new
        teacher-to-course assignment.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_teaching = (t_id, c_id)

        cursor.callproc('add_teaching', new_teaching)


    # Updating existing teaching record (R4)
    @transaction(dictionary=False)
    def update_teaching(self, cursor, conn, tch_id, t_id, c_id):
        """
        Execute 'update_teaching' stored procedure to update the
        teacher-to-course record.
        """
        # Collect parameters into a tuple for the stored procedure call
        updated = (tch_id, t_id, c_id)

        cursor.callproc('update_teaching', updated)


    # Deleting a teaching record (R4)
    @transaction(dictionary=False)
    def delete_teaching(self, cursor, conn, tc_id):
        """
        Execute 'delete_teaching' stored procedure to delete a teaching
        record by ID.
        """
        cursor.callproc('delete_teaching', (tc_id,))