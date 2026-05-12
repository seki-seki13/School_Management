from services.auth_service import AuthService
from services.attendance_service import AttendanceService
from services.student_service import StudentService
from services.schedule_service import ScheduleService
from services.teacher_service import TeacherService
from services.admin_services import AdminService
from services.grade_service import GradesService

from utilities.input_validation import validate_number, validate_input, date_class_validator, course_valid
from utilities.searching import SearchUtils
from utilities.displaying import DisplayUtils

auth_serv = AuthService()
attendance_serv = AttendanceService()
student_serv = StudentService()
schedule_serv = ScheduleService()
teacher_serv = TeacherService()
admin_serv = AdminService()
grade_serv = GradesService()

searcher = SearchUtils()
disp = DisplayUtils()

def profile_info(session):
    while True:
        print('1. View Profile Details\n'
              '2. Change Password\n'
              '3. Go Back')

        action = validate_number('Action: ', 1, 3)
        if action == 3:
            break

        elif action == 1:
            disp.print_user_profile(view_profile(
                session.role, session.pers_id))


        elif action == 2:
            while True:
                old_password = validate_input('Enter Old Password: ')
                valid = auth_serv.login(session.username, old_password)
                if valid:
                    new_password = validate_input('Enter New Password: ')
                    auth_serv.new_password(session.username, new_password)
                    break
                else:
                    ask = input('Try again?(y/n): ')
                    if ask.lower() != 'y':
                        break

def view_profile(role, pers_id):
    data = []
    if role == 'Student':
        data = student_serv.view_all_students()
    elif role == 'Teacher':
        data = teacher_serv.view_all_teachers()
    elif role == 'Admin':
        data = admin_serv.view_all_admins()
    found = searcher.binary_search(data, pers_id, 'pers_id')
    if found:
        return [found]
    else:
        print(f'[!] {role} not found.')


def attendance_menu(role, pers_id):
    data = attendance_serv.get_attendance_by_role(
                role, pers_id)
    if role == 'Student':
        return disp.print_attendance_for_student(data)
    else:
        return disp.print_attendance(data)

def schedule_menu(role, pers_id):
    date = validate_number('1. All Schedule\n'
                           '2. By Date\n'
                           'Choice: ',
                           1, 2)
    if date == 1:
        date = None
    else:
        date = date_class_validator()
    data = schedule_serv.get_my_schedule(role, pers_id, date)
    if role == 'Student':
        return disp.print_schedule(data)
    else:
        return disp.print_schedule_for_teacher(data)

def grades_menu(role, pers_id):
    course_choice = validate_number('1. All Grades\n'
                                   '2. By course\n'
                                   'Choice: ', 1, 2)
    if course_choice == 1:
        course_choice = None
    else:
        course_choice = course_valid('Enter Course ID: ')
    data = grade_serv.get_grades_by_role(role, pers_id, course_choice)
    if role == 'Student':
        return disp.print_grades_for_student(data)
    else:
        return disp.print_grades(data)