# Importing services
from services.attendance_service import AttendanceService
from services.teaching_service import TeachingService
from services.teacher_service import TeacherService
from services.schedule_service import ScheduleService

# Utilities imports: displaying, searching, input validation
from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
from utilities.input_validation import (get_pers_data, validate_number,
                                        course_valid,
                                        date_class_validator)

# Importing submenus
from menus.admin.courses_menu import course_serv
from menus.admin.rooms_menu import room_serv
from menus.shared_menu_options import find_person_ui

# Initialising utility and service instances
disp = DisplayUtils()
searcher = SearchUtils()

attendance_serv = AttendanceService()
teaching_serv = TeachingService()
teacher_serv = TeacherService()
schedule_serv = ScheduleService()


def run_teacher_submenu():
    """
    Manage teacher-related menu.
    Utilises a loop to maintain the session until
    the user decides to return to the main admin menu.
    """
    while True:
        print('\n-- TEACHER SUBMENU --\n'
              '1. Teacher Management\n'
              '2. Teaching\n'
              '3. Schedule\n'
              '4. Go Back')

        choice = validate_number('Select: ')

        # Redirection to chosen submenus
        # if-else structure for choice routing
        if choice == 1: teacher_management()
        elif choice == 2: teaching_management()
        elif choice == 3: schedule_management()
        elif choice == 4: break
        else: print('[!] Invalid choice.')

# ======== 1. TEACHER MANAGEMENT ========

def teacher_management():
    """
    Perform CRUD for Teacher entity.
    Implements Binary Search on loaded data.
    """
    # Actions list: 1 (View), 3 (Find), 4 (Add), 5 (Update), 6 (Delete)
    actions = [1, 3, 4, 5, 6]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Teacher', actions)
        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:  # Go Back
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = teacher_serv.view_all_teachers()
                    disp.print_teachers(data)

                case 3:  # Find (Binary Search)
                    find_person_ui('Teacher')

                case 4:  # Add
                    print('--- Adding Teacher ---')
                    # Collect validated personal details
                    f, l, d, t, a, p, e = get_pers_data()

                    print('--- Login Details ---')
                    while True:
                        try:
                            un = input('Username(>5): ')
                            pw = input('Password(>12): ')

                            # Pass input to the service
                            teacher_serv.add_teacher(
                                f, l, d, t, a, p, e, un, pw)
                            break
                        except Exception as e:
                            print('[!] Invalid Login. Try again')

                case 5: # Update
                    t_id = int(input('Enter ID to Update: '))
                    data = teacher_serv.view_all_teachers()

                    found = searcher.binary_search(
                        data, t_id, 'teacher_id')
                    if found:
                        disp.print_teachers([found])
                        # Collect validated personal details
                        f, l, d, t, a, p, e = get_pers_data()

                        # Pass input to the service
                        teacher_serv.update_teacher(
                            t_id, f, l, d, t, a, p, e)
                    else:
                        print('[!] Teacher not found.')

                case 6: # Delete
                    target = validate_number('Enter ID to Delete: ')

                    # Confirm deletion to prevent accidental cases
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        teacher_serv.delete_teacher(target)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")

# ======== 2. TEACHING MANAGEMENT ========

def teaching_management():
    """
    Perform CRUD for Teaching records.
    """
    # Actions list: 1 (View), 3 (Find), 4 (Add), 5 (Update), 6 (Delete)
    actions = [1, 3, 4, 5, 6]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Teaching', actions)
        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:  # Go Back
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = teaching_serv.view_teaching_records()
                    disp.print_teaching(data)

                case 3:  # Find Course by Teacher
                    # (Stored Procedure + Binary Search)
                    data_teachers = teacher_serv.view_all_teachers()
                    disp.print_teachers(data_teachers)
                    t_id = validate_number('Enter Teacher ID to find: ')
                    data_teaching = teaching_serv.get_my_courses(t_id)
                    found = searcher.binary_search(
                        data_teachers, t_id, 'teacher_id')
                    if found:
                        disp.print_teachers([found])
                    else:
                        print('[!] Teacher not found.')
                    disp.print_courses(data_teaching)


                case 4:  # Add
                    print('--- Assigning Course to Teacher ---')
                    disp.print_teachers(
                        teacher_serv.view_all_teachers())
                    disp.print_courses(
                        course_serv.view_courses())

                    t = validate_number('Teacher ID: ')
                    c = course_valid('Course ID: ')

                    # Pass input to the service
                    teaching_serv.add_teaching(t, c)

                case 5: # Update
                    # Display teaching, teachers and courses records
                    disp.print_teaching(
                        teaching_serv.view_teaching_records())
                    disp.print_teachers(
                        teacher_serv.view_all_teachers())
                    disp.print_courses(
                        course_serv.view_courses())

                    tch = validate_number('Teaching ID to Update: ')
                    t = validate_number('Teacher ID: ')
                    c = course_valid('Course ID: ')

                    # Pass input to the service
                    teaching_serv.update_teaching(tch, t, c)

                case 6: # Delete
                    target = validate_number('Enter ID to Delete: ')

                    # Confirm deletion to prevent accidental cases
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        teaching_serv.delete_teaching(target)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")

# ======== 3. SCHEDULE MANAGEMENT ========

def schedule_management():
    """
    Perform View and Add operations for Schedule records.
    """
    # Actions list: 1 (View), 4 (Add)
    actions = [1, 4]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Schedule', actions)
        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View
                    data = schedule_serv.view_schedule()
                    disp.print_schedule(data)

                case 4:  # Add
                    print('--- Adding Schedule ---')
                    # Display teaching rooms records
                    disp.print_teaching(
                        teaching_serv.view_teaching_records())
                    disp.print_rooms(room_serv.view_rooms())

                    tch = validate_number('Teaching ID: ')
                    r = validate_number('Room ID: ')
                    d = date_class_validator()

                    # Pass input to the service
                    schedule_serv.add_schedule(tch, r, d)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")