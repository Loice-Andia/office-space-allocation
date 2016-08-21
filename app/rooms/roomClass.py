from app.person.personClass import people_data
from app.amity.amityClass import rooms


class Room(object):
    """
    Room
    """

    def __init__(self):
        self.room_name = ""
        self.room_type = ""

    def get_names(self, identifier, people_data):
        if identifier in people_data['Staff'].keys():
            return people_data['Staff'][identifier]['name'].upper()
        elif identifier in people_data['Fellow'].keys():
            return people_data['Fellow'][identifier]['name'].upper()

    def print_room(self, args):
        room_name = args["<room_name>"]

        if room_name in rooms['LivingSpace'].keys():
            for identifier in rooms['LivingSpace'][room_name]:
                print self.get_names(identifier, people_data)
        elif room_name in rooms['Office'].keys():
            for identifier in rooms['Office'][room_name]:
                print self.get_names(identifier, people_data)

    def print_allocations(self, args):
        """
        Loops through the rooms object printing the room and the occupants
        """
        data = ""
        for room_type in rooms.keys():
            data += room_type.upper()
            data += "\n"
            for room_name in rooms[room_type].keys():
                data += room_name.upper()
                data += "----------------------------------------"
                for identifier in rooms[room_type][room_name]:
                    data += self.get_names(identifier, people_data)
                    data += ", "
                data += "\n"

        print data

        if args["--o"]:
            with open(args["--o"], 'wt') as f:
                f.write(data)
                print "The list of allocations has been saved " \
                    "to the following file: "
                print args["--o"]

    def print_unallocated(self, args):
        pass
