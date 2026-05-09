"""
Display Utility - Formats and displays data using tabulate
Handles displaying reports, tables, messages
"""

from tabulate import tabulate


class DisplayUtils:
    """Utility class for displaying data in table format"""

    @staticmethod
    def print_table(title, data, columns):
        """
        Generic method to display ANY list of objects as a table.

        Args:
            title: Title of the table
            data: List of objects to display
            columns: List of tuples: (display_name, attribute_name)
        """
        if not data:
            print(f"\n[!] No records found\n")
            return

        print(f"\n{'=' * 100}")
        print(f"  {title}")
        print(f"{'=' * 100}\n")

        rows = []
        headers = [col[0] for col in columns]

        for item in data:
            row = []
            for _, attr_name in columns:
                try:
                    value = getattr(item, attr_name, "N/A")
                except Exception:
                    value = "N/A"
                row.append(str(value) if value else "N/A")
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="grid"))
        print()

    @staticmethod
    def print_students(students):
        """Display students table"""
        DisplayUtils.print_table(
            "STUDENTS LIST",
            students,
            [
                ("Student ID", "student_id"),
                ("Person ID", "pers_id"),
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Phone", "phone"),
                ("Email", "email")
            ]
        )

    @staticmethod
    def print_teachers(teachers):
        """Display teachers table"""
        DisplayUtils.print_table(
            "TEACHERS LIST",
            teachers,
            [
                ("Teacher ID", "teacher_id"),
                ("Person ID", "pers_id"),
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Phone", "phone"),
                ("Email", "email")
            ]
        )

    @staticmethod
    def print_admins(admins):
        """Display admins table"""
        DisplayUtils.print_table(
            "ADMINS LIST",
            admins,
            [
                ("Admin ID", "admin_id"),
                ("Person ID", "pers_id"),
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Phone", "phone"),
                ("Email", "email")
            ]
        )

    @staticmethod
    def print_courses(courses):
        """Display courses table"""
        DisplayUtils.print_table(
            "COURSES LIST",
            courses,
            [
                ("Course ID", "course_id"),
                ("Course Name", "course_name")
            ]
        )

    @staticmethod
    def print_registrations(registrations):
        """Display registrations table"""
        DisplayUtils.print_table(
            "REGISTRATIONS LIST",
            registrations,
            [
                ("Reg ID", "reg_id"),
                ("Student Name", "st_name"),
                ("Teacher Name", "teacher_name"),
                ("Course", "course_name"),
                ("Reg Date", "reg_date")
            ]
        )

    @staticmethod
    def print_teaching(teaching_records):
        """Display teaching assignments table"""
        DisplayUtils.print_table(
            "TEACHING ASSIGNMENTS",
            teaching_records,
            [
                ("Teaching ID", "tc_id"),
                ("Teacher", "t_name"),
                ("Course", "c_id")
            ]
        )

    @staticmethod
    def print_rooms(rooms):
        """Display rooms table"""
        DisplayUtils.print_table(
            "ROOMS LIST",
            rooms,
            [
                ("Room ID", "room_id"),
                ("Room Label", "room_label"),
                ("Floor", "floor"),
                ("Capacity", "capacity"),
                ("Type", "type_name")
            ]
        )

    @staticmethod
    def print_schedule(schedule_list):
        """Display schedule table"""
        DisplayUtils.print_table(
            "CLASS SCHEDULE",
            schedule_list,
            [
                ("Schedule ID", "teach_course_id"),
                ("Teacher", "teacher_name"),
                ("Course", "course_name"),
                ("Room", "room_label"),
                ("Floor", "floor"),
                ("Capacity", "capacity"),
                ("Type", "type_name"),
                ("Date", "date_class")
            ]
        )

    @staticmethod
    def print_attendance(attendance_list):
        """Display attendance table"""
        if not attendance_list:
            print(f"\n[!] No attendance records found\n")
            return

        print(f"\n{'=' * 80}")
        print(f"  ATTENDANCE RECORDS")
        print(f"{'=' * 80}\n")

        rows = []
        for att in attendance_list:
            rows.append([
                att.course_name,
                str(att.date_class),
                att.student_name,
                att.attendance_status
            ])

        print(tabulate(
            rows,
            headers=["Course", "Date", "Student", "Status"],
            tablefmt="grid"
        ))
        print()

    @staticmethod
    def print_grades(grades_list):
        """Display grades table"""
        if not grades_list:
            print(f"\n[!] No grades found\n")
            return

        print(f"\n{'=' * 80}")
        print(f"  GRADES")
        print(f"{'=' * 80}\n")

        rows = []
        for grade in grades_list:
            rows.append([
                grade.student_name,
                grade.course_name,
                grade.final_grade
            ])

        print(tabulate(
            rows,
            headers=["Student", "Course", "Grade"],
            tablefmt="grid"
        ))
        print()

    # ============ REPORT DISPLAYING ============

    @staticmethod
    def print_students_per_course(report_dict):
        """
        Display students per course report.

        Args:
            report_dict: Dictionary from ReportingUtils.students_per_course()
        """
        if not report_dict:
            print("\n[!] No data to display\n")
            return

        print(f"\n{'=' * 60}")
        print(f"  STUDENTS PER COURSE")
        print(f"{'=' * 60}\n")

        rows = [[course, count] for course, count in report_dict.items()]
        print(tabulate(rows, headers=["Course Name", "Total Students"], tablefmt="grid"))
        print()

    @staticmethod
    def print_average_grades(report_dict):
        """
        Display average grades per course report.

        Args:
            report_dict: Dictionary from ReportingUtils.average_grade_per_course()
        """
        if not report_dict:
            print("\n[!] No data to display\n")
            return

        print(f"\n{'=' * 60}")
        print(f"  AVERAGE GRADE PER COURSE")
        print(f"{'=' * 60}\n")

        rows = [[course, f"{grade:.2f}"] for course, grade in report_dict.items()]
        print(tabulate(rows, headers=["Course Name", "Average Grade"], tablefmt="grid"))
        print()

    @staticmethod
    def print_attendance_summary(report_dict):
        """
        Display attendance summary report.

        Args:
            report_dict: Dictionary from ReportingUtils.attendance_summary()
        """
        if not report_dict:
            print("\n[!] No data to display\n")
            return

        print(f"\n{'=' * 80}")
        print(f"  ATTENDANCE SUMMARY")
        print(f"{'=' * 80}\n")

        rows = [
            [
                course,
                stats['total'],
                stats['present'],
                f"{stats['attendance_percentage']}%"
            ]
            for course, stats in report_dict.items()
        ]

        print(tabulate(
            rows,
            headers=["Course", "Total Records", "Present", "Attendance %"],
            tablefmt="grid"
        ))
        print()

    # ============ MESSAGE METHODS ============

    @staticmethod
    def print_success(message):
        """Print success message"""
        print(f"\n✓ SUCCESS: {message}\n")

    @staticmethod
    def print_error(message):
        """Print error message"""
        print(f"\n✗ ERROR: {message}\n")

    @staticmethod
    def print_warning(message):
        """Print warning message"""
        print(f"\n⚠ WARNING: {message}\n")

    @staticmethod
    def print_info(message):
        """Print info message"""
        print(f"\nℹ INFO: {message}\n")