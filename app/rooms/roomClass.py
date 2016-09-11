from app.person.personClass import people_data
from app.amity.amityClass import rooms


class Room(object):
    """
    Room
    """
    #Replace the '+=' with .format()

    def __init__(self):
        self.room_name = ""
        self.room_type = ""

    def get_names(self, identifier):
        # map(function, sequence)
        # .get(val, msg) to retrieve dict item

        person = people_data.get(identifier, None)
        if person == None:
            return "Person Does not exist"
        return person['name']

    def print_room(self, args):
        room_name = args["<room_name>"]
        # name = rooms.get(identifier, None)

        room = rooms.get(room_name, None)
        if room == None:
            return "{} Does Not Exist".format(room_name)

        occupants = map(self.get_names, room['occupants'])
        print "\n".join(occupants)
        return occupants


    def print_allocations(self, args):
        """
        Loops through the rooms object printing the room and the occupants
        """

        data = ""
        for room in rooms:
            data += "{} \n".format(room.upper())
            data += "-" * 65
            data += "\n"
            if len(rooms[room]['occupants']) is 0:
                data += "No Occupants"
            occupants = map(self.get_names, rooms[room]['occupants'])
            data +=",".join(occupants)


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
                    break
                data += "{}\n".format(self.get_names(person)

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print "Unallocated people have been saved to {} ".format(args["<filename>"])
        return data
