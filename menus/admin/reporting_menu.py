from utilities.input_validation import validate_number
from utilities.reporting import ReportingUtils
from utilities.displaying import DisplayUtils

disp = DisplayUtils()
report = ReportingUtils()

# =========== REPORTING MENU ============

def run_reporting_menu():
    while True:
        print('\n-- REPORTS --\n'
              '1. Students per Course\n'
              '2. Average Grade per Course\n'
              '3. Attendance Summary\n'
              '4. Go Back')
        try:
            choice = validate_number('Select: ')
            if choice == 1:
                disp.print_students_per_course(
                    report.students_per_course())
            elif choice == 2:
                disp.print_average_grades(
                    report.average_grade_per_course())
            elif choice == 3:
                disp.print_attendance_summary(
                    report.attendance_summary())
            elif choice == 4: break
            else: print('[!] Invalid choice.')

        except Exception as e:
            print(f'Invalid input or Error: {e}')