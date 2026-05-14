# Importing validation, reporting, and displaying utilities
from utilities.input_validation import validate_number
from utilities.reporting import ReportingUtils
from utilities.displaying import DisplayUtils

# Initialising utility instances
disp = DisplayUtils()
report = ReportingUtils()


def run_reporting_menu():
    """
    Manage the system reports menu.
    This menu allows administrators to generate and view cross-table
    analytical data regarding enrollment, performance, and attendance.

    Data is automatically sorted via the @sorted_by decorator
    in ReportingUtils.
    """
    while True:
        print('\n-- REPORTS --\n'
              '1. Students per Course\n'
              '2. Average Grade per Course\n'
              '3. Attendance Summary\n'
              '4. Go Back')
        try:
            choice = validate_number('Select: ')

            if choice == 1:
                # Retrieve student counts per course report
                # and pass to display utility
                disp.print_students_per_course(
                    report.students_per_course())

            elif choice == 2:
                # Retrieve average grade per course report
                # and pass to display utility
                disp.print_average_grades(
                    report.average_grade_per_course())

            elif choice == 3:
                # Retrieve attendance summary report
                # and pass to display utility
                disp.print_attendance_summary(
                    report.attendance_summary())

            elif choice == 4: break # Go back to main admin menu

            else: print('[!] Invalid choice.')

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f'Invalid input or Error: {e}')