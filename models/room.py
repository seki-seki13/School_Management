class RoomType:
    """
    Class for room types.
    Provides the foundation for 3NF room entities representation
    through inheritance.
    Encapsulates data and then safely retrieves through @property.
    Input validation is mostly done in database and input layers.
    """
    def __init__(self, type_id, type_name):
        # Primary identifier
        self.__type_id = type_id

        self.__type_name = type_name


    # Allow safe and secure data retrieval
    @property
    def type_id(self):
        return self.__type_id

    @property
    def type_name(self):
        return self.__type_name


class Room(RoomType):
    """
    Subclass representing physical classrooms.
    Inherits categories from the RoomType class.
    Encapsulates data and then safely retrieves through @property.
    Input validation is mostly done in database and input layers.
    """
    def __init__(
            self, room_id, room_label, floor,
            capacity, type_id, type_name):
        # Pass inherited attributes
        super().__init__(type_id=type_id, type_name=type_name)

        # Additional room attributes
        self.__room_id = room_id
        self.__room_label = room_label
        self.__floor = floor

        if capacity < 1:
            raise ValueError('Capacity must be positive')
        self.__capacity = capacity


    # Allow safe and secure data retrieval
    @property
    def room_id(self):
        return self.__room_id

    @property
    def room_label(self):
        return self.__room_label

    @property
    def floor(self):
        return self.__floor

    @property
    def capacity(self):
        return self.__capacity