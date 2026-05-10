from services.admin_services import AdminService
from services.auth_service import AuthService
from services.student_service import StudentService
from services.teacher_service import TeacherService
from services.course_service import CoursesService
from services.teaching_service import TeachingService
from services.grade_service import GradesService
from services.schedule_service import ScheduleService
from services.attendance_service import AttendanceService
from services.registration_service import RegistrationService
from services.room_service import RoomService

from utilities.displaying import DisplayUtils
from utilities.reporting import ReportingUtils
from utilities.searching import SearchUtils

admin_serv = AdminService()
auth_serv = AuthService()
student_serv = StudentService()
teacher_serv = TeacherService()
course_serv = CoursesService()
teaching_serv = TeachingService()
grade_serv = GradesService()
schedule_serv = ScheduleService()
attendance_serv = AttendanceService()
registration_serv = RegistrationService()
room_serv = RoomService()

disp = DisplayUtils()
report = ReportingUtils()
searcher = SearchUtils()


def run_admin_menu(session):
    """The Main Admin loop."""
    while True:
        print(f"\n{'=' * 30}")
        print(f" ADMIN MENU\nWelcome, {session.username}")
        print(f"{'=' * 30}")
        print("1. Manage Admins")
        print("2. Manage Students")
        print("3. Manage Teachers")
        print("4. Manage Authentication")

        try:
            main_choice = int(input("\nSelect category: "))

            if main_choice == 1:
                manage_students()
            elif main_choice == 2:
                manage_teachers()
            elif main_choice == 3:
                # Add manage_courses() later
                print("Course management under construction")
            elif main_choice == 4:
                print("Logging out...")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


def print_crud_options(entity, number_list):
    labels = {1: 'View All', 3: 'Find (Binary Search)', 4: 'Add New', 5: 'Update', 6: 'Delete'}

    print(f"\n--- {entity.upper()} MANAGEMENT ---")
    for i, num in enumerate(number_list, 1):
        print(f"{i}. {labels[num]} {entity}")
    print(f"{len(number_list) + 1}. Go Back")


def manage_students():
    """Explicit logic for Students."""
    # We want these specific actions for students
    actions = [1, 3, 4, 6]

    while True:
        print_crud_options("Student", actions)
        try:
            choice = int(input("Action: "))

            if choice == len(actions) + 1:  # Go Back
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    # The @sorted_by decorator in your service handles the sorting!
                    data = student_serv.view_all_students()
                    disp.print_students(data)

                case 3:  # Find (Binary Search)
                    data = student_serv.view_all_students()
                    s_id = input("Enter Student ID to find: ")
                    # USES YOUR BINARY SEARCH
                    found = searcher.binary_search(data, s_id, 'student_id')
                    if found:
                        disp.print_students([found])  # Wrap in list to print table
                    else:
                        print("[!] Student not found.")

                case 4:  # Add
                    f = input("First Name: ")
                    l = input("Last Name: ")
                    d = input("DOB (YYYY-MM-DD): ")
                    t = input("Town: ")
                    a = input("Address: ")
                    p = input("Phone: ")
                    e = input("Email: ")
                    student_serv.add_student(f, l, d, t, a, p, e)

                case 6:  # Delete
                    target = int(input("Enter ID to delete: "))
                    confirm = input(f"Confirm delete ID {target}? (y/n): ")
                    if confirm.lower() == 'y':
                        student_serv.delete_student(target)

        except Exception as e:
            print(f"Invalid input or Error: {e}")


def manage_teachers():
    """Explicit logic for Teachers."""
    actions = [1, 4, 6]
    while True:
        print_crud_options("Teacher", actions)
        choice = int(input("Action: "))
        if choice == len(actions) + 1: break

        actual_action = actions[choice - 1]
        if actual_action == 1:
            disp.print_teachers(teacher_serv.view_all_teachers())
        elif actual_action == 4:
            # Similar to student input...
            print("Teacher adding logic goes here")
        elif actual_action == 6:
            target = int(input("Enter ID to delete: "))
            teacher_serv.delete_teacher(target)


