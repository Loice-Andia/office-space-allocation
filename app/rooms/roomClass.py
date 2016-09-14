from app.person.personClass import people_data
from app.amity.amityClass import rooms


class Room(object):
    """
    Room
    """
    # Replace the '+=' with .format()

    def __init__(self):
        self.room_name = ""
        self.room_type = ""

    def get_names(self, identifier):
        """
        Gets the name of a person from the people_data dictionary
        """
        # map(function, sequence)
        # .get(val, msg) to retrieve dict item

        person = people_data.get(identifier, None)
        if person == None:
            return "Person Does not exist"
        return person['name']

    def print_room(self, args):
        """
        Prints the name of occupants in a room
        """
        room_name = args["<room_name>"]
        # name = rooms.get(identifier, None)

        message = ""

        room = rooms.get(room_name, None)
        if room == None:
            message += "{} Does Not Exist".format(room_name)
            return message

        occupants = map(self.get_names, room['occupants'])

        message += "\n".join(occupants)
        return message

    def print_allocations(self, args):
        """
        Loops through the rooms object printing the room and the occupants
        """

        data = ""

        for room in rooms:
            room_info = rooms.get(room, None)
            room_type = "Living Space"
            if room_info['is_office']:
                room_type = "Office"
            data += "\n\n{} ({}) \n".format(room.upper(), room_type)
            data += "-" * 65
            data += "\n"
            if len(rooms[room]['occupants']) is 0:
                data += "No Occupants"
            occupants = map(self.get_names, rooms[room]['occupants'])
            data += ",".join(occupants)

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print "Allocations has been saved to {}".format(args["<filename>"])
        return data

    def print_unallocated(self, args):
        """
        Loops through the people_data dictionary
        Checks if an identifier in the people_data has been allocated an office,
        if not prints the name.
        Checks if a persons who wants accomodation has been allocated a living space,
        if not prints the name and missing room
        """
        data = "Those unallocated:\n"

        for person in people_data:
            for room in rooms:
                if person in rooms[room]['occupants']:
                    data += ""
            else:
                data += "{}\n".format(self.get_names(person))

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print "Unallocated people have been saved to {} ".format(args["<filename>"])
        return data
