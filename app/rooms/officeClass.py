from roomClass import Room


class Office(Room):
    """
    Office
    """

    def __init__(self):
        self.room_type = 'Office'
        self.room_capacity = 4
