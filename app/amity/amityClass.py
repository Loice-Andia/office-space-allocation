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
        while room_type not in ['O', 'L']:
            room_type = raw_input(
                "Enter room type: \n o: Office space \n l: Living space: \n")
            room_type = room_type.upper()

        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            if room_type == "O":
                rooms['Office'].update({room: []})
            if room_type == "L":
                rooms['LivingSpace'].update({room: []})

        print "You have created the following rooms: \n"
        print "OFFICES: " + ', '.join(rooms['Office'].keys())
        print "LIVING SPACES: " + ', '.join(rooms['LivingSpace'].keys())

        return rooms
