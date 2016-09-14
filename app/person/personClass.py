import random
from app.amity.amityClass import rooms

people_data = {}


class Person(object):
    """
    Person Class
    """

    def __init__(self):
        self.person_name = ''

    wants_accomodation = 'N'

    def add_person(self, args):
        """
        Adds a person to the People_data dictionary
        allocates the person to a random room.
        """

        person_name = "{} {}".format(args["<first_name>"], args["<last_name>"])
        person_name = person_name.upper()
        message = ""
        wants_accomodation = 'N'
        is_fellow = args['Fellow']
        self.person_identifier = len(people_data) + 1

        if args["<wants_accomodation>"]:
            wants_accomodation = args["<wants_accomodation>"]

        for person in people_data:
            # import ipdb
            # ipdb.set_trace()
            if people_data[person]['name'] == person_name:
                message = "{} Already Exists\n".format(person_name)
                return message

        people_data.update({
            self.person_identifier: {
                'name': person_name,
                'accomodation': wants_accomodation,
                'is_fellow': is_fellow}
        })

        message += self.allocate_rooms(self.person_identifier)

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
        message = ""

        person_identifier = int(args["<person_identifier>"])
        new_room = args["<new_room_name>"]

        person = people_data.get(person_identifier, 'Does not exist')

        # find currently allocated room and remove identifier
        for current_room in rooms:
            if person_identifier in rooms[current_room]['occupants']:
                rooms[current_room]['occupants'].remove(person_identifier)

        # Append identifier to new_room
        rooms[new_room]['occupants'].append(person_identifier)

        message += "{} has been removed from {} and allocated {} room\n".format(
            person['name'], current_room, new_room)
        return message

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
        # print args
        arg_dict = {}
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

                    arg_dict.update({
                        "<first_name>": person[0],
                        "<last_name>": person[1],
                        "Staff": is_staff,
                        "Fellow": is_fellow,
                        "<wants_accomodation>": wants_accomodation
                    })

                    message += self.add_person(arg_dict)
        return message
