# Importing model, database elements and decorators
from models.room import Room, RoomType
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class RoomService:
    """
    Service layer for managing physical classrooms.
    Handles the execution of stored procedures related to the
    Rooms and RoomTypes tables and maps results
    into the corresponding models.

    CRUD: viewing and adding.
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by room type name (R5)
    @sorted_by('type_name')
    @transaction(dictionary=True)
    def v_room_types(self, cursor, conn):
        """
        Execute 'v_room_types' stored procedure to get all room types
        records for administrative management.
        """
        cursor.callproc('v_room_types')
        room_types = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
                r_type = RoomType(
                    type_id=row['type_id'],
                    type_name=row['type_name']
                )
                room_types.append(r_type)
        return room_types


    # Sorting the loaded data by room label (R5)
    @sorted_by('room_label')
    @transaction(dictionary=True)
    def view_rooms(self, cursor, conn):
        """
        Execute 'v_rooms' stored procedure to get all room
        records for administrative managing.
        """
        cursor.callproc('v_rooms')
        rooms = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
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


    # Creating a new room type (R3)
    @transaction(dictionary=False)
    def add_room_type(self, cursor, conn, t_name):
        """
        Execute 'add_room_type' stored procedure to add
        a new room type.
        """
        cursor.callproc('add_room_type', (t_name,))


    # Creating a new classroom (R3)
    @transaction(dictionary=False)
    def add_room(self, cursor, conn, room_label,
                 floor, capacity, type_id):
        """
        Execute 'add_room' stored procedure
        to add a new classroom.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_room = (room_label, floor, capacity, type_id)

        cursor.callproc('add_room', new_room)