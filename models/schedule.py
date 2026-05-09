class Schedule:
    def __init__(self, schedule_id, teach_course_id, room_id, date_class, **kwargs):
        self.__schedule_id = schedule_id
        self.__teach_course_id = teach_course_id
        self.__room_id = room_id
        self.__date_class = date_class

        self.__teacher_name = (f"{kwargs.get('teacher_first_name', '')} "
                               f"{kwargs.get('teacher_last_name', '')}").strip()
        self.__course_name = kwargs.get('course_name', '')
        self.__room_label = kwargs.get('room_label', '')
        self.__floor = kwargs.get('floor', '')
        self.__capacity = kwargs.get('capacity', '')
        self.__type_name = kwargs.get('room_type', '')

    @property
    def schedule_id(self):
        return self.__schedule_id

    @property
    def teach_course_id(self):
        return self.__teach_course_id

    @property
    def room_id(self):
        return self.__room_id

    @property
    def date_class(self):
        return self.__date_class

    @property
    def teacher_name(self):
        return self.__teacher_name

    @property
    def room_label(self):
        return self.__room_label

    @property
    def floor(self):
        return self.__floor

    @property
    def capacity(self):
        return self.__capacity

    @property
    def type_name(self):
        return self.__type_name