from roomClass import Room


class LivingSpace(Room):
    """
    LivingSpace
    """

    max_capacity = 6

    def __init__(self, room_capacity, occupants=[]):
        self.room_capacity = room_capacity
        self.occupants = occupants
