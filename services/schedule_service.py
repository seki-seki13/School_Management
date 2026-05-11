from models.schedule import Schedule
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class ScheduleService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('date_class')
    @transaction(dictionary=True)
    def view_schedule(self, cursor, conn):
        cursor.callproc('v_schedule')
        schedule = []
        for result in cursor.stored_results():
            for row in result.fetchall():
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

    @sorted_by('date_class')
    @transaction(dictionary=True)
    def get_my_schedule(self, cursor, conn, role, pers_id, date=None):
        schedule = []
        if role == 'Teacher':
            cursor.callproc('f_teacher_schedule', (pers_id, date))
            for result in cursor.stored_results():
                for row in result.fetchall():
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
            cursor.callproc('f_stud_schedule', (pers_id, date))
            for result in cursor.stored_results():
                for row in result.fetchall():
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

    @transaction(dictionary=False)
    def add_schedule(self, cursor, conn, tc_id, room_id, class_date):
        new_schedule = (tc_id, room_id, class_date)
        cursor.callproc('add_schedule', new_schedule)