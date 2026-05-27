# Importing validation service, utilities and common menu options
from services.teaching_service import TeachingService
from services.grade_service import GradesService
from utilities.input_validation import (validate_number, course_valid,
                                        grade_valid)
from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from menus.shared_menu_options import (profile_info, attendance_menu,
                                       schedule_menu)

# Initialise instances
teaching_serv = TeachingService()
grade_serv = GradesService()
disp = DisplayUtils()
searcher = SearchUtils()


def run_teach_menu(session):
    """
        Manage the Teacher portal.

        Uses loop for continuous execution.
        Input is validated with the validation utility (R7).
    """

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

            elif action == 5:
                print('Logging out...')
                break

            # Manage sessions and redirecting to specific menus
            # if-else structure for choice routing
            elif action == 1:
                # First display courses, then detailed schedule
                courses_data = teaching_serv.get_my_courses(
                    pers_id=session.pers_id)
                disp.print_courses(courses_data)
                schedule_menu(session.role, session.pers_id)

            elif action == 2:
                attendance_menu(session.role, session.pers_id)

            elif action == 3:
                while True:
                    choice = validate_number('1. View all Grades\n'
                                             '2. View grades by course\n'
                                             '3. Add a grade\n'
                                             '4. Update a grade\n'
                                             '5. Back\n'
                                             'Choice: ')
                    if choice == 5:
                        break
                    elif choice == 1: # View all
                        data = grade_serv.get_grades_by_role(
                            session.role, session.pers_id)
                        disp.print_grades(data)

                    elif choice == 2: # View by course
                        while True:
                            courses_data = teaching_serv.get_my_courses(
                                pers_id=session.pers_id)
                            disp.print_courses(courses_data)
                            c_id = course_valid('Course ID: ')

                            # Find if this teacher teaches this course
                            found = searcher.binary_search(
                                courses_data, c_id, 'course_id')
                            if not found:
                                print('No grades found')
                            else:
                                data = grade_serv.get_grades_by_role(
                                    session.role, session.pers_id,
                                    course_id=c_id)
                                disp.print_grades(data)

                    elif choice == 3: # Add
                        data = grade_serv.f_reg_for_grade(session.pers_id)
                        disp.print_grades(data)

                        while True:
                            reg_id = validate_number(
                                'Registration ID to grade: ')

                            # Find if such a registration exists
                            found = searcher.binary_search(
                                data, reg_id, 'reg_id')

                            if not found:
                                print(f'There is no {reg_id} ID')
                            else:
                                grade = grade_valid()
                                grade_serv.add_grade(reg_id, grade)
                                print('Grade added')
                                break

                    elif choice == 4: # Update
                        data = grade_serv.f_reg_for_grade(session.pers_id)
                        disp.print_grades(data)

                        while True:
                            reg_id = validate_number(
                                'Registration ID to update grade: ')

                            # Find if such a registration exists
                            found = searcher.binary_search(
                                data, reg_id, 'reg_id')

                            if not found:
                                print(f'There is no {reg_id} ID')
                            else:
                                grade = grade_valid()
                                grade_serv.update_grade(reg_id, grade)
                                print('Grade updated')
                                break


            elif action == 4:
                profile_info(session)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f'[!] Invalid input or Error: {e}')