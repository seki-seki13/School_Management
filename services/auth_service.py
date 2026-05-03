from database.connection import DatabaseConnection
from models.authentication import Authentication
from mysql.connector import Error

class AuthService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    def login(self, e_username, e_password):
        conn = self.database_manager.connect()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                
                # Check if the user exists and get person id
                cursor.callproc('get_auth_by_username', (e_username,))
                auth_data = None

                for fetched_data in cursor.stored_results():
                    auth_data = fetched_data.fetchone()

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
                    print('\n[!] Invalid username or password.')
                    return None

            except Error as e:
                raise ValueError(f'Error: {e}')
            finally:
                self.database_manager.close_conn()