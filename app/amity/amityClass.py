rooms = {
    'Office': {},
    'LivingSpace': {}
}


class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        # self.rooms = {
        #     'Office': [],
        #     'LivingSpace': []
        # }

    def create_room(self, args):
        """Allows user to enter a list of room names specifying
                whether office or living spaces"""

        room_type = None

        # Assign a group of rooms to a room type
        if room_type is None:
            room_type = raw_input(
                "Enter room type: \n O: Office space \n L: Living space: \n")
            room_type = room_type.upper()
            while room_type != "O" and room_type != "L":
                room_type = raw_input(
                    "Try again. Enter Room Type:\n O: Office space \n L: Living space: \n")
  
        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            if room_type == "O":
                rooms['Office'].update({room: []})
            elif room_type == "L":
                rooms['LivingSpace'].update({room: []})

        return rooms

    def save_state(self):
        pass

    def load_state(self):
        pass
