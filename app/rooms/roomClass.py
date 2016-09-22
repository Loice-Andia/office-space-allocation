from app.person.personClass import people_data
from app.amity.amityClass import rooms


class Room(object):
    """
    This is the Room class that has all functions that display data
    from the rooms dict.
    METHODS
    ---------------------------------
    get_names method:
        Takes up the person's id as aa param and returns the name of the
        person from the people_data dictionary
    print_room method:
        Takes the room_name from the args passed and prints the names of
        occupants in the room.
    print_allocations method:
        Takes up the filename as an optional argument.
        For every room, it prints out the names of the occupants in the room.
        If filename is provided, it saves data to the file
    print_unallocated method:
        Takes up the filename as an optional argument.
        Compares the occupants in each room to the people dictionary,
        if a person has not been allocated the relevant room, prints out the name.
        If filename is provided, it saves data to the file

    """

    def get_names(self, identifier):
        """
        Gets the name of a person from the people_data dictionary
        """

        person = people_data.get(identifier, None)
        if person == None:
            return "Person Does not exist"
        return person['name']

    def print_room(self, args):
        """
        Prints the name of occupants in a room
        """
        room_name = args["<room_name>"].upper()

        room = rooms.get(room_name, None)
        if room == None:
            message = "{} Does Not Exist".format(room_name)
            return message

        message = "{}\n".format(room_name.upper())
        message += "-" * 30
        message +="\n"

        if not room['occupants']:
            message += "No Occupants"
            return message

        occupants = list(map(self.get_names, room['occupants']))

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
            data += "\n".join(occupants)

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print("Allocations has been saved to {}".format(
                    args["<filename>"]))
        return data

    def print_unallocated(self, args):
        """
        Loops through the people_data dictionary
        Checks if an identifier in the people_data
        has been allocated an office,
        if not prints the name.
        Checks if a persons who wants accomodation
        has been allocated a living space,
        if not prints the name and missing room
        """
        data = ""

        office_allocations = []
        living_space_allocations = []
        people_without_living_spaces = []

        for room_name, room_info in rooms.items():
            if room_info['is_office']:
                office_allocations += room_info['occupants']
            if not room_info['is_office']:
                living_space_allocations += room_info['occupants']

        unallocated_offices = list(
            set(people_data.keys()) - set(office_allocations))
        people_without_offices = list(map(self.get_names, unallocated_offices))

        data += "Those unallocated Offices:\n"
        if len(people_without_offices):
            data += "\n".join(people_without_offices)
        else:
            data += "NONE"

        data += "\n\nThose unallocated living spaces:\n"

        for person_id, person_info in people_data.items():
            if person_info['is_fellow'] and person_info['accomodation'] == 'Y':
                if person_id not in living_space_allocations:
                    people_without_living_spaces.append(person_info['name'])

        if len(people_without_living_spaces):
            data += "\n".join(people_without_living_spaces)
        else:
            data += "NONE"

        if args["-o"]:
            with open(args["<filename>"], 'wt') as output_file:
                output_file.write(data)
                print("Unallocated people have been saved to {} ".format(
                    args["<filename>"]))
        return data
