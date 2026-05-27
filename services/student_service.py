# Importing model, database elements and decorators
from models.student import Student
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class StudentService:
    """
    Service layer for managing student records.
    Handles the execution of stored procedures related to the
    Students table and maps results into the corresponding model.

    CRUD: full CRUD (R4).
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Stacked decorators: 1. @transaction, 2. @sorted_by
    # Sorting the loaded data by last name (R5)
    @sorted_by('last_name')
    @transaction(dictionary=True) # rows as {key: value}
    def view_all_students(self, cursor, conn):
        """
        Execute 'v_students' stored procedure to get all students
        records for administrative management.
        """
        cursor.callproc('v_students')
        students = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                # Instantiating the model
                stud = Student(
                    stud_id=row['stud_id'],
                    pers_id=row['pers_id'],
                    f_name=row['first_name'],
                    l_name=row['last_name'],
                    dob=row['DoB'],
                    town=row['town'],
                    address=row['address'],
                    phone=row['phone'],
                    email=row['email']
                )
                students.append(stud) # Build list of model objects
        return students


    # Creating a new student with authentication (R4)
    @transaction(dictionary=False)
    def add_student(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email,
            e_username, e_password):
        """
        Execute 'add_student' stored procedure to create a new
        student and login credentials.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_student = (f_name,l_name, dob, e_town,
                       e_address, e_phone, e_email,
                       e_username, e_password)
        cursor.callproc('add_student', new_student)


    # Updating student's personal information (R4)
    # @transaction decorator handles connection, cursor,
    # commit/rollback automatically — keeps method clean
    @transaction(dictionary=False)
    def update_student(self, cursor, conn, s_id, f_name, l_name,
                       dob, e_town, e_address, e_phone, e_email):
        """
        Calls 'update_student' stored procedure to update
        an existing student record in the database.
        cursor and conn are injected by the @transaction decorator.
        """
        # Pack all update parameters into a tuple
        # Tuples are immutable — safe to pass as procedure arguments
        updated = (s_id, f_name, l_name,
                   dob, e_town, e_address, e_phone, e_email)

        # Execute the stored procedure with the parameter tuple
        cursor.callproc('update_student', updated)


    # Deleting a student record (R4)
    @transaction(dictionary=True)
    def delete_student(self, cursor, conn, s_id):
        """
        Execute 'delete_student' stored procedure to delete an entity
        with student ID via ON DELETE CASCADE.
        """
        cursor.callproc('delete_student', (s_id,))