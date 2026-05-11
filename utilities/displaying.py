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
        """
        if not data:
            print(f"\n[!] No records found for {title}\n")
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
                    # getattr looks for the @property names you defined in your models
                    value = getattr(item, attr_name, "N/A")
                except Exception:
                    value = "N/A"
                row.append(str(value) if value is not None else "N/A")
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        print()

    @staticmethod
    def print_user_profile(profile):
        DisplayUtils.print_table(
            'PROFILE INFORMATION',
            profile,
            [
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "birth_date"),
                ("Town", "town"),
                ("Address", "address"),
                ("Phone", "phone"),
                ("Email", "email")
            ])

    @staticmethod
    def print_students(students):
        """Display students table"""
        DisplayUtils.print_table(
            "STUDENTS LIST",
            students,
            [
                ("Student ID", "student_id"),
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Address", "address"),
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
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Address", "address"),
                ("Phone", "phone"),
                ("Email", "email")
            ]
        )

    @staticmethod
    def print_admins(admins):
        """Display teachers table"""
        DisplayUtils.print_table(
            "ADMINS LIST",
            admins,
            [
                ("Admin ID", "admin_id"),
                ("First Name", "first_name"),
                ("Last Name", "last_name"),
                ("DOB", "dob"),
                ("Town", "town"),
                ("Address", "address"),
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
                ("Student", "st_name"),
                ("Teacher", "teacher_name"),
                ("Course", "course_name"),
                ("Date", "reg_date")
            ]
        )

    @staticmethod
    def print_teaching(teaching_records):
        """Display teaching assignments (Teacher + Course)"""
        DisplayUtils.print_table(
            "TEACHING ASSIGNMENTS",
            teaching_records,
            [
                ("ID", "tc_id"),
                ("Teacher", "t_name"),
                ("Course", "course_name") # Returns course_name from your property
            ]
        )

    @staticmethod
    def print_rooms_types(rooms):
        """Display rooms table"""
        DisplayUtils.print_table(
            "ROOM TYPES LIST",
            rooms,
            [
                ("Type ID", "type_id"),
                ("Type", "type_name")
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
                ("Label", "room_label"),
                ("Floor", "floor"),
                ("Capacity", "capacity"),
                ("Type", "type_name")
            ]
        )

    @staticmethod
    def print_schedule(schedule_list):
        """Display schedule table (Updated with schedule_id)"""
        DisplayUtils.print_table(
            "SCHEDULE",
            schedule_list,
            [
                ("ID", "schedule_id"),
                ("Course", "course_name"),
                ("Teacher", "teacher_name"),
                ("Room", "room_label"),
                ("Type", "type_name"),
                ("Date", "date_class")
            ]
        )

    @staticmethod
    def print_attendance(attendance_list):
        """Display attendance table"""
        DisplayUtils.print_table(
            "ATTENDANCE RECORDS",
            attendance_list,
            [
                ("Student", "student_name"),
                ("Course", "course_name"),
                ("Date", "date_class"),
                ("Status", "attendance_status")
            ]
        )

    @staticmethod
    def print_grades(grades_list):
        """Display grades table"""
        DisplayUtils.print_table(
            "GRADES",
            grades_list,
            [
                ('Registration ID', 'reg_id'),
                ("Student", "student_name"),
                ("Course", "course_name"),
                ("Final Grade", "final_grade")
            ]
        )

    # ============ REPORT DISPLAYING ============

    @staticmethod
    def print_students_per_course(report):
        if not report:
            print("\n[!] No data to display\n")
            return

        rows = [[rep.course_name, rep.total_students] for rep in report]
        print(tabulate(rows,
                       headers=["Course Name", "Total Students"],
                       tablefmt="fancy_grid"))

    @staticmethod
    def print_average_grades(report):
        if not report:
            print("\n[!] No data to display\n")
            return

        rows = [[rep.course_name, f"{rep.average_grade:.2f}" if rep.average_grade else "N/A"]
                for rep in report]
        print(tabulate(rows,
                       headers=["Course Name", "Average Grade"],
                       tablefmt="fancy_grid"))

    @staticmethod
    def print_attendance_summary(report):
        if not report:
            print("\n[!] No data to display\n")
            return

        rows = [[rep.course_name, rep.total_records,
                f'{rep.attendance_percentage}%'
                if rep.attendance_percentage else '0%']
                for rep in report]

        print(tabulate(rows,
                       headers=['Course', 'Total Records', 'Attendance %'],
                       tablefmt='fancy_grid'))
        print()