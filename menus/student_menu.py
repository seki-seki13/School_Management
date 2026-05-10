from services.attendance_service import AttendanceService
from services.grade_service import GradesService
from services.schedule_service import ScheduleService
from services.auth_service import AuthService

from utilities.displaying import DisplayUtils

def run_stud_menu(session):

    attendance_serv = AttendanceService()
    grade_serv = GradesService()
    schedule_serv = ScheduleService()
    auth_serv = AuthService()
    print('Student Menu Loading Successful')

    while True:
        print(f'\n{'-'*30}')
        print(' Student Menu\n')
        print(f' Welcome, {session.username}')
        print(f'{'-' * 30}\n')

        print('1. Schedule\n'
              '2. Grades\n'
              '3. Attendance\n'
              '4. My Profile\n'
              '5. Change Password\n'
              '6. Logout')

        options = [1, 2, 3, 4, 5, 6]
        try:
            action = int(input('Selected: '))
            if action not in options:
                print(f'There is no [{action}] option. Try again.\n')
            else:
                if action == 6:
                    print('Logging out...')
                    break

                elif action == 1:
                    data = schedule_serv.get_my_schedule(
                        session.role, session.pers_id)
                    DisplayUtils.print_schedule(data)

                elif action == 2:
                    data = grade_serv.get_grades_by_role(
                        session.role, session.pers_id)
                    DisplayUtils.print_grades(data)

                elif action == 3:
                    data = attendance_serv.get_attendance_by_role(
                        session.role, session.pers_id)
                    DisplayUtils.print_attendance(data)

                elif action == 4:
                    data = auth_serv.get_user_profile(session.pers_id)
                    DisplayUtils.print_user_profile(data)

                elif action == 5:
                    try:
                        old_password = input('Enter Old Password: ')
                        auth_serv.login(session.username, old_password)

                        new_password = input('Enter New Password: ')
                        auth_serv.new_password(session.username, new_password)

                    except Exception as e:
                        print('Invalid Password')

        except Exception as e:
            print(f'Error: {e}')