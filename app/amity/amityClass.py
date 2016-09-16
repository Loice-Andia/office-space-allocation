
rooms = {}


class Amity(object):
    """

    This is the main Amity class.
    It has the get_room_type and create_room methods.
    get_room_type method:
        gets input from the user on the room type and returns the room_type.
    create_room method:
        gets the list of room_names to be added from the args passed
        gets the room_type from the get_room_type method
        Saves the rooms created in the rooms dictionary
    sample rooms dictionary:
        rooms = {
            1:{'name': 'LILAC', 'occupants':[]},
            2:{'name': 'VALHALLA', 'occupants':[]},
        }

    """

    def get_room_type(self, room_type=None):
        """

        This method gets the room_type from the user
        after running the create_room command.

        """
        room_type = room_type

        # Assign a group of rooms to a room type
        while room_type not in ['O', 'L']:
            room_type = raw_input(
                "Enter room type: \n o: Office space \n l: Living space: \n")
            room_type = room_type.upper()
        return room_type

    def create_room(self, args, room_type=None):
        """

        Allows user to enter a list of room names specifying
        whether office or living spaces and adds them to the rooms dict

        """

        room_type = room_type

        room_type = self.get_room_type(room_type)
        is_office = False

        if room_type == 'O':
            is_office = True

        # Adds room to the rooms dict
        for room in args["<room_name>"]:
            if room.upper() in rooms:
                message = "{} Exists\n".format(room.upper())
                return message

            rooms.update({room.upper(): {
                "occupants": [], "is_office": is_office}
            })

        message = "You have the following rooms:\n "
        message += '\n'.join(rooms.keys())

        return message
