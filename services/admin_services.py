# Importing model, database elements and decorators
from models.admin import Administration
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class AdminService:
    """
    Service layer for managing administration staff.
    Handles the execution of stored procedures related to the
    Administration table and maps results into
    the corresponding model.

    CRUD: viewing and adding.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by last name (R5)
    @sorted_by('last_name')
    @transaction(dictionary=True)
    def view_all_admins(self, cursor, conn):
        """
        Execute 'v_admins' stored procedure to get all admins
        records for administrative management.
        """
        cursor.callproc('v_admins')
        admins = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                # Instantiating the model
                admin = Administration(
                    admin_id=row['admin_id'],
                    pers_id=row['pers_id'],
                    f_name=row['first_name'],
                    l_name=row['last_name'],
                    dob=row['DoB'],
                    town=row['town'],
                    address=row['address'],
                    phone=row['phone'],
                    email=row['email']
                )
                admins.append(admin)
        return admins


    # Creating a new administrative record with authentication (R4)
    @transaction(dictionary=False)
    def add_admin(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email,
            e_username, e_password):
        """
        Execute 'add_admin' stored procedure to create a new
        administration staff member and login credentials.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_admin = (f_name, l_name, dob, e_town,
                     e_address, e_phone, e_email,
                     e_username, e_password)

        cursor.callproc('add_admin', new_admin)