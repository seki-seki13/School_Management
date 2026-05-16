# Importing model, database elements and a decorator
from models.authentication import Authentication
from database.connection import DatabaseConnection
from utilities.decorators import transaction

class AuthService:
    """
    Service layer for managing authentication records.
    Handles the execution of login operation and setting new password.

    CRUD: updating.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()


    # Managing logining process
    @transaction(dictionary=True)
    def login(self, cursor, conn, e_username, e_password):
        """
        Handle logining in process executing 'get_auth_by_username'
        and 'get_user_role' stored procedures to verify the user.
        This process then determines the user's level of authority.
        """
        # 1. Check if the user exists and get person id
        cursor.callproc('get_auth_by_username', (e_username,))
        auth_data = None

        # Fetch one matching record
        for fetched_data in cursor.stored_results():
            auth_data = fetched_data.fetchone()

        # 2. Verify password
        if auth_data and auth_data['password'] == e_password:
            p_id = auth_data['pers_id']

            # 3. Get the role based on person id
            cursor.callproc('get_user_role', (p_id,))

            # Identify user's role for authorization
            found_role = 'None'
            for result in cursor.stored_results():
                res = result.fetchone()
                found_role = res['role']

            # Notification
            print(f'Successfully logged in as {found_role}')

            # Return an authentication object
            return Authentication(
                auth_id = None, # Not required for sessions
                pers_id = p_id,
                username = e_username,
                password = e_password,
                role = found_role
            )

        else:
            print('\n[!] Invalid username or password. [!]')
            return None


    # Updating the password (R4)
    @transaction(dictionary=False)
    def new_password(self, cursor, conn, e_username, new_pass):
        """
        Execute 'update_password' stored procedure to modify
        user's credentials.
        """
        # Collect parameters into a tuple for the procedure call
        new_password = (e_username, new_pass)

        cursor.callproc('update_password', new_password)