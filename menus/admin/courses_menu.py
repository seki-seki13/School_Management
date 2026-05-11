from services.course_service import CoursesService
from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
from utilities.input_validation import (course_valid, validate_input,
                                        validate_number)

disp = DisplayUtils()
searcher = SearchUtils()
course_serv = CoursesService()

#========= COURSES MANAGEMENT ==============

def run_courses_menu():
    actions = [1, 3, 4, 5, 6]

    while True:
        print_crud_options('Course', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:  # Go Back
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = course_serv.view_courses()
                    disp.print_courses(data)

                case 3:  # Find (Binary Search)
                    data = course_serv.view_courses()
                    c_id = course_valid('Enter Course ID to find: ')
                    found = searcher.binary_search(
                        data, c_id, 'course_id')
                    if found:
                        disp.print_courses([found])
                    else:
                        print('[!] Course not found.')

                case 4:  # Add
                    print('--- Adding Course ---')
                    while True:
                        try:
                            cid = course_valid('Course ID: ')
                            cn = validate_input('Course Name: ')
                            course_serv.add_course(cid, cn)
                            break
                        except Exception as e:
                            print(f'[!] Invalid input or Error: {e}')


                case 5:
                    c_id = course_valid('Enter ID to Update: ')
                    cn = validate_number('Course Name: ')
                    course_serv.update_course(c_id, cn)

                case 6:
                    target = course_valid('Enter ID to Delete: ')
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        course_serv.delete_course(target)

        except Exception as e:
            print(f"Invalid input or Error: {e}")