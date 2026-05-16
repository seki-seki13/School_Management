# Importing model, database elements and decorators
from models.registration import Registration
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class RegistrationService:
    """
    Service layer for managing students' registration records.
    Handles the execution of stored procedures related to the
    Registration table and maps results into the corresponding model.

    CRUD: full CRUD (R4).
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by registration date (R5)
    @sorted_by('reg_date')
    @transaction(dictionary=True)
    def view_registration(self, cursor, conn):
        """
        Execute 'v_registration' stored procedure
        to get all registration records for administrative management.
        """
        cursor.callproc('v_registration')
        registration_records = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
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


    # Getting registration records based on student's ID
    @transaction(dictionary=True)
    def find_registration_by_student(self, cursor, conn, stud_id):
        """
        Execute 'f_registration' stored procedure to get a specific
        student's registration records.
        """
        cursor.callproc('f_registration', (stud_id,))
        records = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                # Instantiating the model
                reg = Registration(
                    reg_id=row['registration_ID'],
                    stud_id=stud_id,
                    teach_course_id=None,
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    teacher_first_name=row['teacher_first_name'],
                    teacher_last_name=row['teacher_last_name'],
                    course_name=row['course_name'],
                    reg_date=row['reg_date']
                )
                records.append(reg)
        return records


    # Creating a new registration record by registering
    # a student to a teaching record (R4)
    @transaction(dictionary=False)
    def add_registration(self, cursor, conn, s_id, tc_id):
        """
        Execute 'add_registration' stored procedure to add a
        new registration record.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_reg = (s_id, tc_id)

        cursor.callproc('add_registration', new_reg)


    # Updating a registration record
    # by reassigning student and teaching IDs (R4)
    @transaction(dictionary=False)
    def update_registration(self, cursor, conn, r_id, new_s_id, new_tc_id):
        """
        Execute 'update_registration' stored procedure to update
        an existing registration record.
        """
        # Collect parameters into a tuple for the stored procedure call
        updated = (r_id, new_s_id, new_tc_id)

        cursor.callproc('update_registration', updated)


    # Deleting a registration record (R3)
    @transaction(dictionary=False)
    def delete_registration(self, cursor, conn, r_id):
        """
        Execute 'delete_registration' stored procedure to delete
        a registration record.
        """
        cursor.callproc('delete_registration', (r_id,))