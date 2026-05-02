class RoomType:
    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name


class Room(RoomType):
    def __init__(
            self, room_id, room_label, floor, capacity, type_id, type_name):
        super().__init__(type_id, type_name)

        self.room_id = room_id
        self.room_label = room_label
        self.floor = floor

        if capacity < 1:
            raise ValueError('Capacity must be positive')
        self.capacity = capacity
