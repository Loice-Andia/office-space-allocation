from roomClass import Room


class Office(Room):
    """
    Office
    """
    max_capacity = 4

    def __init__(self, room_capacity, occupants=[]):
        self.room_capacity = room_capacity
        self.occupants_num = occupants
