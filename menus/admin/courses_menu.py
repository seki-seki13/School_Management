# Importing service layer for course-related database operations
from services.course_service import CoursesService
# Importing display, search, and formatting utilities
from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
# Importing specialized input validation functions for course data
from utilities.input_validation import (course_valid, validate_input,
                                        validate_number)

# Initialising utility and service instances for the module
disp = DisplayUtils()
searcher = SearchUtils()
course_serv = CoursesService()


def run_courses_menu():
    """
    Manage the course menu.
    Uses a loop to allow multiple operations and implements
    match-case for efficient navigation of CRUD actions.
    """
    # Actions list: 1 (View), 3 (Find), 4 (Add), 5 (Update), 6 (Delete)
    actions = [1, 3, 4, 5, 6]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Course', actions)

        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:  # Go Back
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = course_serv.view_courses()
                    disp.print_courses(data)

                case 3:  # Find (Binary Search)
                    # Load data into memory
                    data = course_serv.view_courses()
                    c_id = course_valid('Enter Course ID to find: ')

                    # Utilise Binary Search
                    found = searcher.binary_search(
                        data, c_id, 'course_id')
                    if found:
                        disp.print_courses([found])
                    else:
                        print('[!] Course not found.')

                case 4:  # Add
                    print('--- Adding Course ---')
                    # Nested loop for ensuring valid record is added

                    while True:
                        try:
                            cid = course_valid('Course ID: ')
                            cn = validate_input('Course Name: ')
                            course_serv.add_course(cid, cn)
                            break
                        # Catch unexpected errors
                        except Exception as e:
                            print(f'[!] Invalid input or Error: {e}')


                case 5: # Update
                    c_id = course_valid('Enter ID to Update: ')
                    cn = validate_input('Course Name: ')
                    course_serv.update_course(c_id, cn)

                case 6: # Delete
                    target = course_valid('Enter ID to Delete: ')

                    # Confirm deletion to prevent accidental cases
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        course_serv.delete_course(target)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")