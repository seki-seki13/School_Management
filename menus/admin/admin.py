from menus.admin.student_submenu import run_student_submenu
from menus.admin.teacher_submenu import run_teacher_submenu
from menus.admin.courses_menu import run_courses_menu
from menus.admin.rooms_menu import run_rooms_submenu
from menus.admin.reporting_menu import run_reporting_menu
from menus.admin.admin_menu import run_admin_menu
from utilities.input_validation import validate_number
from utilities.displaying import DisplayUtils
from menus.shared_menu_options import profile_info

disp = DisplayUtils()

# ==============================================
# ============== MAIN MENU =====================

def run_admin(session):
    while True:
        print(f'\n{'=' * 30}\n'
              ' ADMIN MENU\n'
              f' Welcome, {session.username}\n'
              f'{'=' * 30}\n')

        print('1. Administration Management\n'
              '2. Student Management '
              '(Registration, Grades, Attendance)\n'
              '3. Teacher Management '
              '(Teaching, Schedule)\n'
              '4. Courses Management\n'
              '5. Rooms Management\n'
              '6. Reports\n'
              '7. My Profile\n'
              '8. Logout')

        try:
            main_choice = validate_number('\nSelect category[1-8]: ')

            if main_choice == 1: run_admin_menu()
            elif main_choice == 2: run_student_submenu()
            elif main_choice == 3: run_teacher_submenu()
            elif main_choice == 4: run_courses_menu()
            elif main_choice == 5: run_rooms_submenu()
            elif main_choice == 6: run_reporting_menu()
            elif main_choice == 7: profile_info(session)
            elif main_choice == 8:
                print('Logging out...')
                break
            else: print('[!] Invalid choice.')

        except ValueError:
            print('[!] Input must be a number.')