from models.teacher import Teacher
from database.connection import DatabaseConnection, transaction

class TeacherService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_all_teachers(self, cursor, conn):
        cursor.callproc('v_teachers')
        teachers = []
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
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

    @transaction(dictionary=False)
    def add_teacher(
            self, cursor, conn, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        new_teacher = (f_name, l_name, dob, e_town, e_address, e_phone, e_email)
        cursor.callproc('add_teacher', new_teacher)

    @transaction(dictionary=False)
    def update_teacher(self, cursor, conn, t_id, f_name, l_name,
            dob, e_town, e_address, e_phone, e_email):
        updated = (t_id, f_name, l_name, dob, e_town, e_address, e_phone, e_email)
        cursor.callproc('update_teacher', updated)

    @transaction(dictionary=False)
    def delete_teacher(self, cursor, conn, t_id):
        cursor.callproc('delete_teacher', (t_id,))