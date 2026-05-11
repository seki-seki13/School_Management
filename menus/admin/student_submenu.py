from services.student_service import StudentService
from services.registration_service import RegistrationService
from services.grade_service import GradesService
from services.attendance_service import AttendanceService
from services.schedule_service import ScheduleService

from menus.admin.teacher_submenu import teaching_serv

from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
from utilities.input_validation import (get_pers_data,
                                        validate_number, grade_valid)

disp = DisplayUtils()
searcher = SearchUtils()
student_serv = StudentService()
registration_serv = RegistrationService()
grade_serv = GradesService()
attendance_serv = AttendanceService()
schedule_serv = ScheduleService()

#============= 2. STUDENT SUBMENU ===============
# (Student/Registration/Attendance/Grades Management)

def run_student_submenu():
    while True:
        print('\n-- STUDENT SUBMENU --\n'
              '1. Student Management\n'
              '2. Registration\n'
              '3. Attendance\n'
              '4. Grades\n'
              '5. Go Back')
        choice = validate_number('Select: ')
        if choice == 1: student_management()
        elif choice == 2: registration_management()
        elif choice == 3: attendance_management()
        elif choice == 4: grades_management()
        elif choice == 5: break
        else: print('[!] Invalid choice.')

# ======== 1. STUDENT MANAGEMENT ========

def student_management():
    actions = [1, 3, 4, 5, 6]
    while True:
        print_crud_options('Student', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:  # Go Back
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = student_serv.view_all_students()
                    disp.print_students(data)

                case 3:  # Find (Binary Search)
                    data = student_serv.view_all_students()
                    s_id = validate_number('Enter Student ID to find: ')
                    found = searcher.binary_search(
                        data, s_id, 'student_id')
                    if found:
                        disp.print_students([found])
                    else:
                        print('[!] Student not found.')

                case 4:  # Add
                    print('--- Adding Student ---')
                    f, l, d, t, a, p, e = get_pers_data()
                    print('--- Login Details ---')
                    while True:
                        try:
                            un = input('Username(>5): ')
                            pw = input('Password(>12): ')
                            student_serv.add_student(f, l, d, t, a, p, e, un, pw)
                        except Exception as e:
                            print('[!] Invalid Login. Try again')

                case 5: # Update
                    s_id = validate_number('Enter ID to Update: ')
                    data = student_serv.view_all_students()
                    found = searcher.binary_search(
                        data, s_id, 'student_id')
                    if found:
                        disp.print_students([found])
                        f, l, d, t, a, p, e = get_pers_data()
                        student_serv.update_student(s_id, f, l, d, t, a, p, e)
                    else:
                        print('[!] Student not found.')


                case 6:
                    target = validate_number('Enter ID to Delete: ')
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        student_serv.delete_student(target)

        except Exception as e:
            print(f"Invalid input or Error: {e}")

# ======== 2. REGISTRATION MANAGEMENT ========

def registration_management():
    actions = [1, 3, 4, 5, 6]
    while True:
        print_crud_options('Registration', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:  # Go Back
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = registration_serv.view_registration()
                    disp.print_registrations(data)

                case 3:  # Find (Stored Procedure)
                    disp.print_students(student_serv.view_all_students())
                    s_id = validate_number('Enter Student ID to find: ')
                    found = (registration_serv.
                             find_registration_by_student(s_id))
                    if found:
                        disp.print_registrations(found)
                    else:
                        print('[!] Registration not found.')

                case 4:  # Add
                    print('--- Adding Registration ---')
                    disp.print_students(
                        student_serv.view_all_students())
                    disp.print_teaching(
                        teaching_serv.view_teaching_records())
                    s = validate_number('Student ID: ')
                    tch = validate_number('Teaching ID: ')

                    registration_serv.add_registration(s, tch)

                case 5:
                    r_id = validate_number('Enter ID to Update: ')
                    found = (registration_serv.
                             find_registration_by_student(r_id))
                    if found:
                        disp.print_registrations([found])
                        disp.print_students(
                            student_serv.view_all_students())
                        disp.print_teaching(
                            teaching_serv.view_teaching_records())
                        s = validate_number('Student ID: ')
                        tch = validate_number('Teaching ID: ')

                        registration_serv.update_registration(r_id, s, tch)
                    else:
                        print('[!] Registration not found.')

                case 6:
                    target = validate_number('Enter ID to Delete: ')
                    confirm = input(f'Confirm delete ID {target}?(y/n)')
                    if confirm.lower() != 'y':
                        print('Deletion Canceled')
                    else:
                        registration_serv.delete_registration(target)

        except Exception as e:
            print(f"Invalid input or Error: {e}")

# ======== 3. ATTENDANCE MANAGEMENT ========

def attendance_management():
    actions = [1, 4]
    while True:
        print_crud_options('Attendance', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1: # View
                    data = attendance_serv.view_attendance()
                    disp.print_attendance(data)

                case 4: # Add
                    print('--- Adding Attendance ---')
                    disp.print_schedule(
                        schedule_serv.view_schedule())
                    disp.print_students(
                        student_serv.view_all_students())
                    sch = validate_number('Schedule ID: ')
                    s = validate_number('Student ID: ')
                    a = validate_number('2 = Present | '
                                  '1 = Late | '
                                  '0 = Absent\n'
                                  'Attendance: ', 0, 2)
                    attendance_serv.add_attendance(sch, s, a)

        except Exception as e:
            print(f'[!] Invalid input or Error: {e}')

# ======== 4. GRADES MANAGEMENT ========

def grades_management():
    actions = [1, 4, 5]
    while True:
        print_crud_options('Grade', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:
                break

            actual_action = actions[choice - 1]
            match actual_action:
                case 1: # View
                    data = grade_serv.view_grades()
                    disp.print_grades(data)

                case 4: # Add
                    print('--- Adding Grade ---')
                    disp.print_registrations(
                        registration_serv.view_registration())
                    r = validate_number('Registration ID: ')
                    g = grade_valid()
                    grade_serv.add_grade(r, g)

                case 5:
                    disp.print_grades(grade_serv.view_grades())
                    r = validate_number('Registration ID to Update: ')
                    g = grade_valid()
                    grade_serv.update_grade(r, g)

        except Exception as e:
            print(f'[!] Invalid input or Error: {e}')