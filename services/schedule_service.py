from models.schedule import Schedule
from database.connection import DatabaseConnection, transaction

class ScheduleService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @transaction(dictionary=True)
    def view_schedule(self, cursor, conn):
        cursor.callproc('v_schedule')
        schedule = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                sch = Schedule(
                    teach_course_id=row['teach_course_id'],
                    room_id=row['room_id'],
                    date_class=row['date_class'],
                    teacher_first_name=row['teacher_first_name'],
                    teacher_last_name=row['teacher_last_name'],
                    course_name=row['course_name'],
                    room_type=row['room_type'],
                    room_label=row['room_label'],
                    floor=row['floor'],
                    capacity=row['capacity'],
                )
                schedule.append(sch)
        return schedule

    @transaction(dictionary=False)
    def add_schedule(self, cursor, conn, tc_id, room_id, class_date):
        new_schedule = (tc_id, room_id, class_date)
        cursor.callproc('add_schedule', new_schedule)