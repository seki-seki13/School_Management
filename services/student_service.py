from database.connection import DatabaseConnection, transaction
from models.student import Student

class StudentService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_all_students(self, cursor, conn):
        cursor.callproc('v_students')
        students = []
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
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
                students.append(stud)
        return students


    @transaction(dictionary=True)
    def add_student(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        new_student = (f_name,l_name, dob, e_town,
                       e_address, e_phone, e_email)
        cursor.callproc('add_student', new_student)

    @transaction(dictionary=False)
    def update_student(self, cursor, conn, s_id, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        updated = (s_id, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email)
        cursor.callproc('update_student', updated)

    @transaction(dictionary=True)
    def delete_student(self, cursor, conn, s_id):
        cursor.callproc('delete_student', (s_id,))