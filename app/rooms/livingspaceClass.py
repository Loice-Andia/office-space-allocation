from roomClass import Room


class LivingSpace(Room):
    """
    LivingSpace
    """

    max_capacity = 6

    def __init__(self, occupants=[]):
        self.room_type = 'LivingSpace'
        self.room_capacity = 6
        self.occupants = occupants
