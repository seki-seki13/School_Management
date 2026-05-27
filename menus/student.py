# Importing validation utilities and common menu options
from utilities.input_validation import validate_number
from menus.shared_menu_options import (profile_info, attendance_menu,
                                       schedule_menu)
from services.grade_service import GradesService
from utilities.displaying import DisplayUtils


def run_stud_menu(session):
    """
    Manage the Student portal.

    Uses loop for continuous execution.
    Input is validated with the validation utility (R7).
    """
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

            elif action == 5:
                    print('Logging out...')
                    break

            # Redirecting to specific menus
            # if-else structure for choice routing
            elif action == 1:
                schedule_menu(session.role, session.pers_id)

            elif action == 2:
                grade_serv = GradesService()
                disp = DisplayUtils()
                data = grade_serv.get_grades_by_role(session.role, session.pers_id)
                disp.print_grades_for_student(data)

            elif action == 3:
                attendance_menu(session.role, session.pers_id)

            elif action == 4:
                profile_info(session)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f'[!] Invalid input or Error: {e}')