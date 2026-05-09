from models.grades import Grade
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class GradesService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('student_name')
    @transaction(dictionary=True)
    def view_grades(self, cursor, conn):
        cursor.callproc('v_grades')
        grades = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                gr = Grade(
                    grade_id=None,
                    reg_id=None,
                    final_grade=row['final_grade'],
                    student_first_name=row['student_first_name'],
                    student_last_name=row['student_last_name'],
                    course_name=row['course_name']
                )
                grades.append(gr)
        return grades

    @sorted_by('final_grade', reverse=True)
    @transaction(dictionary=True)
    def get_grades_by_role(self, cursor, conn, role, pers_id, course_id=None):
        grades = []
        if role == 'Teacher':
            cursor.callproc('f_grades_teacher', (pers_id, course_id))
            for result in cursor.stored_results():
                for row in result.fetchall():
                    gr = Grade(
                        grade_id=None,
                        reg_id=None,
                        final_grade=row['final_grade'],
                        student_first_name=row['student_first_name'],
                        student_last_name=row['student_last_name'],
                        course_name=row['course_name']
                    )
                    grades.append(gr)
        else:
            cursor.callproc('f_grades_student', (pers_id,))
            for result in cursor.stored_results():
                for row in result.fetchall():
                    gr = Grade(
                        grade_id=None,
                        reg_id=None,
                        final_grade=row['final_grade'],
                        student_first_name=None,
                        student_last_name=None,
                        course_name=row['course_name']
                    )
                    grades.append(gr)
            return grades
        return grades


    @transaction(dictionary=False)
    def add_grade(self, cursor, conn, r_id, f_gr):
        new_grade = (r_id, f_gr)
        cursor.callproc('add_grade', new_grade)

    @transaction(dictionary=False)
    def update_grade(self, cursor, conn, r_id, grade):
        updated = (r_id, grade)
        cursor.callproc('update_grade', updated)