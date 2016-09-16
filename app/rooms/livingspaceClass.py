from roomClass import Room


class LivingSpace(Room):
    """

    This is the LivingSpace class that inherits from the Room class.
    It declares the room_type as an 'LivingSpace' and sets the room
    capacity to 6.

    """

    def __init__(self):
        self.room_type = 'LivingSpace'
        self.room_capacity = 6
