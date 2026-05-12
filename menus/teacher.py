from services.teaching_service import TeachingService
from utilities.input_validation import validate_number
from menus.shared_menu_options import (profile_info, attendance_menu,
                                       schedule_menu, grades_menu)

from utilities.displaying import DisplayUtils

teaching_serv = TeachingService()
disp = DisplayUtils()

def run_teach_menu(session):


    print('Teacher Menu Loading Successful')
    while True:
        print(f'\n{'=' * 30}\n'
              ' Teacher Menu\n'
              f' Welcome, {session.username}\n'
              f'{'=' * 30}\n')

        print('1. Courses and Schedule\n'
              '2. Attendance\n'
              '3. Grades\n'
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
                    courses_data = teaching_serv.get_my_courses(session.pers_id)
                    disp.print_courses(courses_data)

                    schedule_menu(session.role, session.pers_id)

                elif action == 2:
                    attendance_menu(session.role, session.pers_id)

                elif action == 3:
                    grades_menu(session.role, session.pers_id)

                elif action == 4:
                    profile_info(session)

        except Exception as e:
            print(f'Error: {e}')