rooms = {}


class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        # self.rooms = {
        #     'Office': [],
        #     'LivingSpace': []
        # }

    def get_room_type(self):
        # Get the room_type from the user
        room_type = None

        # Assign a group of rooms to a room type
        while room_type not in ['O', 'L']:
            room_type = raw_input(
                "Enter room type: \n o: Office space \n l: Living space: \n")
            room_type = room_type.upper()
        return room_type

    def create_room(self, args):
        """Allows user to enter a list of room names specifying
                whether office or living spaces"""

        message = ""

        room_type = self.get_room_type()
        is_office = False

        if room_type == 'O':
            is_office = True

        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            existing_rooms = rooms.get(room, None)
            if existing_rooms != None:
                message += "{} Exists".format(room)
                return message

            rooms.update({room: {"occupants": [], "is_office": is_office}})

        message += "You have the following rooms:\n "
        message += '\n'.join(rooms.keys())

        return message
