# Importing model, database elements and decorators
from models.schedule import Schedule
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class ScheduleService:
    """
    Service layer for managing schedule records.
    Handles the execution of stored procedures related to the
    Schedule table and maps results into the corresponding model.

    CRUD: viewing and adding.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by date of the class (R5)
    @sorted_by('date_class')
    @transaction(dictionary=True)
    def view_schedule(self, cursor, conn):
        """
        Execute 'v_schedule' stored procedure to get all schedule
        records for administrative management.
        """
        cursor.callproc('v_schedule')
        schedule = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
                sch = Schedule(
                    schedule_id=row['schedule_id'],
                    teach_course_id=None,
                    room_id=None,
                    date_class=row['date_class'],
                    teacher_first_name=row['teacher_first_name'],
                    teacher_last_name=row['teacher_last_name'],
                    course_name=row['course_name'],
                    room_type=row['room_type'],
                    room_label=row['room_label'],
                    floor=row['floor'],
                    capacity=row['capacity']
                )
                schedule.append(sch)
        return schedule


    # Getting schedule records based on current session and
    # sorting the loaded data by date of the class (R5)
    @sorted_by('date_class')
    @transaction(dictionary=True)
    def get_my_schedule(self, cursor, conn, role, pers_id, date_class=None):
        """
        Execute current session-specific schedule displaying.
        Stored procedures: 'f_teacher_schedule' and 'f_stud_schedule'.
        Ensures data integrity and ensures accessibility matching
        the authority level.
        """
        schedule = []
        # Role-based accessibility
        if role == 'Teacher':
            cursor.callproc('f_teacher_schedule', (pers_id, date_class))

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
                    sch = Schedule(
                        schedule_id=row['schedule_id'],
                        teach_course_id=None,
                        room_id=None,
                        date_class=row['date_class'],
                        teacher_first_name=None,
                        teacher_last_name=None,
                        course_name=row['course_name'],
                        room_type=row['room_type'],
                        room_label=row['room_label'],
                        floor=None,
                        capacity=None
                    )
                    schedule.append(sch)

        else:
            cursor.callproc('f_stud_schedule', (pers_id, date_class))

            # Iterate through the stored procedure results
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Instantiating the model
                    sch = Schedule(
                        schedule_id=row['schedule_id'],
                        teach_course_id=None,
                        room_id=None,
                        date_class=row['date_class'],
                        teacher_first_name=row['teacher_first_name'],
                        teacher_last_name=row['teacher_last_name'],
                        course_name=row['course_name'],
                        room_type=row['room_type'],
                        room_label=row['room_label'],
                        floor=None,
                        capacity=None
                    )
                    schedule.append(sch)
        return schedule


    # Creating a new schedule record (R3)
    @transaction(dictionary=False)
    def add_schedule(self, cursor, conn, tc_id, room_id, class_date):
        """
        Execute 'add_schedule' stored procedure to add a new schedule
        record by assigning a room to a teaching record
        on a specific date.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_schedule = (tc_id, room_id, class_date)

        cursor.callproc('add_schedule', new_schedule)