from models.authentication import Authentication
from database.connection import DatabaseConnection
from utilities.decorators import transaction

class AuthService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def login(self, cursor, conn, e_username, e_password):
        # Check if the user exists and get person id
        cursor.callproc('get_auth_by_username', (e_username,))
        auth_data = None

        for fetched_data in cursor.stored_results():
            auth_data = fetched_data.fetchone()

        # Verify password
        if auth_data and auth_data['password'] == e_password:
            p_id = auth_data['pers_id']

            # Get the role based on person id
            cursor.callproc('get_user_role', (p_id,))

            found_role = 'None'
            for result in cursor.stored_results():
                res = result.fetchone()
                found_role = res['role']

            print(f'Successfully logged in as {found_role}')
            return Authentication(
                auth_id = None,
                pers_id = p_id,
                username = e_username,
                password = e_password,
                role = found_role
            )

        else:
            print('\n[!] Invalid username or password. [!]')
            return None

    @transaction(dictionary=False)
    def new_password(self, cursor, conn, e_username, new_pass):
        new_password = (e_username, new_pass)
        cursor.callproc('update_password', new_password)

    @transaction(dictionary=True)
    def get_user_profile(self, cursor, conn, pers_id):
        cursor.callproc('f_user_data', (pers_id,))
        for result in cursor.stored_results():
            return result.fetchone()  # Returns the person's info as a dict