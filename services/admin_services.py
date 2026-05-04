from models.admin import Administration
from database.connection import DatabaseConnection, transaction

class AdminService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_all_admins(self, cursor, conn):
        cursor.callproc('v_admins')
        admins = []

        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
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

    @transaction(dictionary=False)
    def add_admin(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        new_admin = (f_name, l_name, dob, e_town,
                     e_address, e_phone, e_email)
        cursor.callproc('add_admin', new_admin)