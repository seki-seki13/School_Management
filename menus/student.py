from services.grade_service import GradesService
from services.schedule_service import ScheduleService

from utilities.displaying import DisplayUtils
from utilities.input_validation import validate_number, validate_input
from menus.shared_menu_options import profile_info, attendance_menu, schedule_menu, grades_menu


def run_stud_menu(session):
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
              '5. Logout')

        options = [1, 2, 3, 4, 5]
        try:
            action = validate_number('Selected: ')
            if action not in options:
                print(f'There is no [{action}] option. Try again.\n')
            else:
                if action == 5:
                    print('Logging out...')
                    break

                elif action == 1:
                    schedule_menu(session.role, session.pers_id)

                elif action == 2:
                    grades_menu(session.role, session.pers_id)

                elif action == 3:
                    attendance_menu(session.role, session.pers_id)

                elif action == 4:
                    profile = profile_info(session)
                    disp.print_students(profile)

        except Exception as e:
            print(f'Error: {e}')