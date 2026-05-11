from services.attendance_service import AttendanceService
from services.grade_service import GradesService
from services.schedule_service import ScheduleService
from services.auth_service import AuthService
from services.student_service import StudentService

from utilities.displaying import DisplayUtils
from utilities.input_validation import validate_number, validate_input
from utilities.searching import SearchUtils

def run_stud_menu(session):
    attendance_serv = AttendanceService()
    grade_serv = GradesService()
    schedule_serv = ScheduleService()
    auth_serv = AuthService()
    student_serv = StudentService()

    searcher = SearchUtils()
    disp = DisplayUtils()

    print('Student Menu Loading Successful')
    while True:
        print(f'\n{'=' * 30}\n'
              ' Student Menu\n'
              f' Welcome, {session.username}\n'
              f'{'=' * 30}\n')

        print('1. Schedule\n'
              '2. Grades\n'
              '3. Attendance\n'
              '4. My Profile\n'
              '5. Change Password\n'
              '6. Logout')

        options = [1, 2, 3, 4, 5, 6]
        try:
            action = validate_number('Selected: ')
            if action not in options:
                print(f'There is no [{action}] option. Try again.\n')
            else:
                if action == 6:
                    print('Logging out...')
                    break

                elif action == 1:
                    data = schedule_serv.get_my_schedule(
                        session.role, session.pers_id)
                    disp.print_schedule(data)

                elif action == 2:
                    data = grade_serv.get_grades_by_role(
                        session.role, session.pers_id)
                    disp.print_grades(data)

                elif action == 3:
                    data = attendance_serv.get_attendance_by_role(
                        session.role, session.pers_id)
                    disp.print_attendance(data)

                elif action == 4:
                    data = student_serv.view_all_students()
                    found = searcher.binary_search(
                        data, session.pers_id, 'pers_id')
                    if found:
                        disp.print_students([found])
                    else:
                        print('[!] Student not found.')

                elif action == 5:
                    while True:
                        old_password = validate_input('Enter Old Password: ')
                        valid = auth_serv.login(session.username, old_password)
                        if valid:
                            new_password = validate_input('Enter New Password: ')
                            auth_serv.new_password(
                                session.username, new_password)
                            break
                        else:
                            ask = input('Try again?(y/n): ')
                            if ask.lower() != 'y':
                                break



        except Exception as e:
            print(f'Error: {e}')