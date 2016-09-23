import random
from app.amity.amityClass import rooms

people_data = {}


class Person(object):
    """

    This is the Person class that has all methods of adding a person,
    loading people from a text file and allocating them rooms.
    sample people_data dictionary:
        people_data = {
            1:{'name': 'LOICE ANDIA', 'is_fellow': True, 'accomodation': 'Y'},
            2:{'name': 'JOHN DOE', 'is_fellow': False, 'accomodation': 'N'},
        }
    METHODS
    --------------------------------
    add_person method:
        Takes up the person's name, role and if one wants accomodation
        from the args passed.
        It checks if the person already exist, if not add the person to
        the people dict and calls the allocate_rooms method
    allocate_rooms method:
        Takes the person identifier as a param.
        It then allocates the person an office and allocates living spaces
        to the people who are fellows and want accomodation
    reallocate_person method:
        Takes up the person's id and room name from the args passed.
        It removes the id from the current room and appends to the new room.
    load_people method:
        Takes up the filename from the args passed.
        Opens the file and reads the line then adds the persons details to an
        args dictionary.
        Calls the add_person method with the args dict to add the people and
        allocate rooms.

    """

    def __init__(self):
        self.person_name = None

    def add_person(self, args):
        """
        Adds a person to the People_data dictionary
        allocates the person to a random room.
        """

        person_name = "{} {}".format(args["<first_name>"], args["<last_name>"])
        person_name = person_name.upper()
        wants_accomodation = 'N'
        is_fellow = args['Fellow']

        self.person_identifier = len(people_data) + 1

        if args["<wants_accomodation>"]:
            wants_accomodation = args["<wants_accomodation>"]

        for person in people_data:
            if people_data[person]['name'] == person_name:
                message = "{} Already Exists\n".format(person_name)
                return message

        people_data.update({
            self.person_identifier: {
                'name': person_name,
                'accomodation': wants_accomodation,
                'is_fellow': is_fellow}
        })

        message = self.allocate_rooms(self.person_identifier)

        return message

    def allocate_rooms(self, identifier):
        """
        Checks available offices
        Checks which living spaces are available
        Randomly picks a room and appends the person identifier
        Checks if the person is a fellow and wants accomodation

        """

        available_living_spaces = []
        available_offices = []

        allocated_office = "No"
        allocated_living_space = "No"
        person = people_data.get(identifier, None)

        for room in rooms:
            if rooms[room]['is_office'] and len(rooms[room]['occupants']) < 4:
                available_offices.append(room)
            if not rooms[room]['is_office'] and len(rooms[room]['occupants']) < 6:
                available_living_spaces.append(room)

        if len(available_offices) > 0:
            allocated_office = random.choice(available_offices)
            rooms[allocated_office]['occupants'].append(identifier)

        if person['accomodation'] == 'Y':
            if person['is_fellow'] and len(available_living_spaces) > 0:
                allocated_living_space = random.choice(available_living_spaces)
                rooms[allocated_living_space]['occupants'].append(identifier)

        message = "{} has been allocated {} office and {} livingSpace\n".format(
            people_data[identifier]['name'], allocated_office,
            allocated_living_space)

        return message

    def reallocate_person(self, args):
        """
        Deletes the person identifier in the current room
        and appends it to the new room
        """

        person_name = args["<person_name>"].upper()
        new_room = args["<new_room_name>"].upper()

        for person in people_data:
            if person_name in people_data[person]['name']:
                person_identifier = person

        # find currently allocated room and remove identifier

        for current_room in rooms:
            if (rooms[new_room]['is_office'] and rooms[current_room]['is_office']) or (not rooms[new_room]['is_office'] and not rooms[current_room]['is_office']):
                if person_identifier in rooms[current_room]['occupants']:
                    rooms[current_room]['occupants'].remove(person_identifier)

        # Append identifier to new_room
        if rooms[new_room]['is_office'] and len(rooms[new_room]['occupants']) < 4:
            rooms[new_room]['occupants'].append(person_identifier)
            message = "{} has been reallocated {} room\n".format(
                person_name, new_room)
            return message
        if not rooms[new_room]['is_office'] and len(rooms[new_room]['occupants']) < 6:
            if people_data[person_identifier]['is_fellow']:
                rooms[new_room]['occupants'].append(person_identifier)
                message = "{} has been reallocated {} room\n".format(
                    person_name, new_room)
                return message
            if not people_data[person_identifier]['is_fellow']:
                return "STAFF CANNOT BE ALLOCATED LIVING SPACES"
        return "{} is full".format(new_room)

    def remove_person(self, args):
        """
        Remove a person from the room
        """

        for person_id, person_info in people_data.items():
            if args["<person_name>"].upper() in person_info['name']:
                if people_data.pop(person_id):
                    for current_room in rooms:
                        if person_id in rooms[current_room]['occupants']:
                            rooms[current_room]['occupants'].remove(person_id)

                    return "{} has been deleted".format(
                        args["<person_name>"].upper())
        return "{} not found".format(args["<person_name>"].upper())

    def load_people(self, args):
        """
        Adds people to rooms from a txt file
        Sample Input Format:

                OLUWAFEMI SULE FELLOW Y
                DOMINIC WALTERS STAFF
                SIMON PATTERSON FELLOW Y
                MARI LAWRENCE FELLOW Y
                LEIGH RILEY STAFF
                TANA LOPEZ FELLOW Y
                KELLY McGUIRE STAFF N
        """
        message = ""

        with open(args["<filename>"], 'r') as input_file:
            people = input_file.readlines()
            for person in people:
                person = person.split()
                if person:
                    is_fellow = True
                    is_staff = False
                    wants_accomodation = None

                    if 'STAFF' in person:
                        is_fellow = False
                        is_staff = True

                    if 'Y' in person:
                        wants_accomodation = 'Y'

                    arg_dict = ({
                        "<first_name>": person[0],
                        "<last_name>": person[1],
                        "Staff": is_staff,
                        "Fellow": is_fellow,
                        "<wants_accomodation>": wants_accomodation
                    })

                    message += self.add_person(arg_dict)
        return message
