# Service imports handle stored procedures execution
from services.auth_service import AuthService
from services.attendance_service import AttendanceService
from services.student_service import StudentService
from services.schedule_service import ScheduleService
from services.teacher_service import TeacherService
from services.admin_services import AdminService
from services.grade_service import GradesService

# Utilities imports for validation, searching and displaying
from utilities.input_validation import (validate_number, validate_input,
                                        date_class_validator, course_valid)
from utilities.searching import SearchUtils
from utilities.displaying import DisplayUtils

# Initialising instances
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
    """
    Function shared among all user types.
    Handles personal profile display and password update
    with current password verification.
    """
    while True:
        print('1. View Profile Details\n'
              '2. Change Password\n'
              '3. Go Back')

        action = validate_number('Action: ', 1, 3)
        if action == 3:
            # Exit
            break

        elif action == 1:
            # Call for view_profile function and print the details
            disp.print_user_profile(view_profile(
                session.role, session.pers_id))

        elif action == 2:
            while True:
                old_password = validate_input('Enter Old Password: ')
                # Check old password correctness for security purposes
                valid = auth_serv.login(session.username, old_password)
                if valid:
                    new_password = validate_input('Enter New Password: ')
                    auth_serv.new_password(session.username, new_password)
                    break
                # Allow more attempts if failed
                else:
                    ask = input('Try again?(y/n): ')
                    if ask.lower() != 'y':
                        break


def view_profile(role, pers_id):
    """
    Get profile data according to the current user.
    (R5) Utilises Binary Search algorithm to find specific record
    within the list.
    """
    data = []
    # Role check
    if role == 'Student':
        data = student_serv.view_all_students()
    elif role == 'Teacher':
        data = teacher_serv.view_all_teachers()
    elif role == 'Admin':
        data = admin_serv.view_all_admins()

    # Perform Binary Search
    found = searcher.binary_search(data, pers_id, 'pers_id')
    if found:
        return [found]
    # Return a user-friendly error if no match
    else:
        print(f'[!] {role} not found.')


def attendance_menu(role, pers_id):
    """
    Retrieve and display attendance according to the current user.
    """
    data = attendance_serv.get_attendance_by_role(
                role, pers_id)
    # Role check
    if role == 'Student':
        return disp.print_attendance_for_student(data)
    else: # Teacher
        return disp.print_attendance(data)


def schedule_menu(role, pers_id):
    """
    Retrieve and display attendance according to the current user.
    Provides filtering options: full schedule or by date.
    """
    date = validate_number('1. All Schedule\n'
                           '2. By Date\n'
                           'Choice: ',
                           1, 2)
    # Exclude optional requirement if 'All'
    if date == 1:
        date = None
    else:
        date = date_class_validator()
    data = schedule_serv.get_my_schedule(role, pers_id, date)

    # Role check
    if role == 'Student':
        return disp.print_schedule(data)
    else: # Teacher
        return disp.print_schedule_for_teacher(data)


def grades_menu(role, pers_id):
    """
    Retrieve and display attendance according to the current user.
    Provides filtering options:
    Student: full grades list;
    Teacher: full grades list or by course.
    """
    # Role check
    if role == 'Student':
        data = grade_serv.get_grades_by_role(role, pers_id)
        return disp.print_grades_for_student(data)
    else:  # Teacher
        course_choice = validate_number('1. All Grades\n'
                                   '2. By course\n'
                                   'Choice: ', 1, 2)
        
        # Exclude optional requirement if 'All'
        if course_choice == 1:
            course_choice = None
        else:
            course_choice = course_valid('Enter Course ID: ')
        data = grade_serv.get_grades_by_role(role, pers_id, course_choice)

        return disp.print_grades(data)




def find_person_ui(role):
    """
    Generic UI for finding a person (Student, Teacher, or Admin).
    Demonstrates search algorithms on loaded data (R5).
    """
    # 1. Get search criteria from user
    print(f'\n--- Find {role} ---')
    print('1. By ID\n2. By First Name\n3. By Last Name\n4. Go Back')
    choice = validate_number('Choice: ', 1, 4)

    if choice == 4:
        return

    # 2. Map choice to the correct model attribute
    attr_map = {
        1: f'{role.lower()}_id',
        2: 'first_name',
        3: 'last_name'
    }
    target_attr = attr_map[choice]

    # 3. Get the target value from the user
    target_val = input(f'Enter {target_attr.replace("_", " ")}: ').strip()

    # 4. Fetch data using the appropriate service
    if role == 'Student':
        data = student_serv.view_all_students()
    elif role == 'Teacher':
        data = teacher_serv.view_all_teachers()
    else:
        data = admin_serv.view_all_admins()

    # 5. Execute Binary Search
    found = searcher.binary_search(data, target_val, target_attr)

    # 6. Display results
    if found:
        if role == 'Student':
            disp.print_students([found])
        elif role == 'Teacher':
            disp.print_teachers([found])
        else:
            disp.print_admins([found])
    else:
        print(f'[!] No {role} found with '
              f'{target_attr.replace("_", " ")}: {target_val}')