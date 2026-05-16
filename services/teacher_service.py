# Importing model, database elements and decorators
from models.teacher import Teacher
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class TeacherService:
    """
    Service layer for managing teacher records.
    Handles the execution of stored procedures related to the
    Teachers table and maps results into the corresponding model.

    CRUD: full CRUD (R4).
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by last name (R5)
    @sorted_by('last_name')
    @transaction(dictionary=True)
    def view_all_teachers(self, cursor, conn):
        """
        Execute 'v_teachers' stored procedure to get all teacher
        records for administrative management.
        """
        cursor.callproc('v_teachers')
        teachers = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                # Instantiating the model
                teacher = Teacher(
                    teacher_id=row['teacher_id'],
                    pers_id=row['pers_id'],
                    f_name=row['first_name'],
                    l_name=row['last_name'],
                    dob=row['DoB'],
                    town=row['town'],
                    address=row['address'],
                    phone=row['phone'],
                    email=row['email']
                )
                teachers.append(teacher)
        return teachers


    # Creating a new teacher with authentication (R4)
    @transaction(dictionary=False)
    def add_teacher(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email,
            e_username, e_password):
        """
        Execute 'add_teacher' stored procedure to create a new
        teacher and login credentials.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_teacher = (f_name, l_name, dob, e_town,
                       e_address, e_phone, e_email,
                       e_username, e_password)

        cursor.callproc('add_teacher', new_teacher)


    # Updating teacher's personal information (R4)
    @transaction(dictionary=False)
    def update_teacher(self, cursor, conn, t_id, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        """
        Execute 'update_teacher' stored procedure to
        update an existing teacher's data.
        """
        # Collect parameters into a tuple for the stored procedure call
        updated = (t_id, f_name, l_name, dob, e_town,
                   e_address, e_phone, e_email)

        cursor.callproc('update_teacher', updated)


    # Deleting a teacher record (R4)
    @transaction(dictionary=False)
    def delete_teacher(self, cursor, conn, t_id):
        """
        Execute 'delete_teacher' stored procedure to delete an entity
        with teacher ID via ON DELETE CASCADE.
        """
        cursor.callproc('delete_teacher', (t_id,))