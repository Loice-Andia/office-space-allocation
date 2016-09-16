from roomClass import Room


class Office(Room):
    """

    This is the Office class that inherits from the Room class.
    It declares the room_type as an 'office' and sets the room
    capacity to 4.

    """

    def __init__(self):
        self.room_type = 'Office'
        self.room_capacity = 4
