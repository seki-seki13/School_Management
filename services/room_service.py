from models.room import Room, RoomType
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by

class RoomService:
    def __init__(self):
        self.database_manager = DatabaseConnection()

    @sorted_by('type_name')
    @transaction(dictionary=True)
    def v_room_types(self, cursor, conn):
        cursor.callproc('v_room_types')
        room_types = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                r_type = RoomType(
                    type_id=row['type_id'],
                    type_name=row['type_name']
                )
                room_types.append(r_type)
        return room_types

    @sorted_by('room_label')
    @transaction(dictionary=True)
    def view_rooms(self, cursor, conn):
        cursor.callproc('v_rooms')
        rooms = []
        for result in cursor.stored_results():
            for row in result.fetchall():
                room = Room(
                    type_id=row['type_id'],
                    room_id=row['room_id'],
                    room_label=row['room_label'],
                    floor=row['floor'],
                    capacity=row['capacity'],
                    type_name=row['type']
                )
                rooms.append(room)
        return rooms

    @transaction(dictionary=False)
    def add_room_type(self, cursor, conn, t_name):
        cursor.callproc('add_room_type', (t_name,))

    @transaction(dictionary=False)
    def add_room(self, cursor, conn, room_label,
                 floor, capacity, type_id):
        new_room = (room_label, floor, capacity, type_id)
        cursor.callproc('add_room', new_room)