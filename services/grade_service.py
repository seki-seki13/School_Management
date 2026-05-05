from models.grades import Grade
from database.connection import DatabaseConnection, transaction

class GradesService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_grades(self, cursor, conn):
        cursor.callproc('v_grades')
        grades = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                gr = Grade(
                    grade_id=None,
                    reg_id=None,
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    course_name=row['course_name'],
                    final_grade=row['final_grade']
                )
                grades.append(gr)
        return grades

    @transaction(dictionary=False)
    def add_grade(self, cursor, conn, r_id, f_gr):
        new_grade = (r_id, f_gr)
        cursor.callproc('add_grade', new_grade)

    @transaction(dictionary=False)
    def update_grade(self, cursor, conn, r_id, grade):
        updated = (r_id, grade)
        cursor.callproc('update_grade', updated)