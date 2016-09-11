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

    def set_default_id(self):
        """
        Gets previous existing ids and sets the max as default
        """
        identifier = 1
        if people_data.keys():
            identifier = max(people_data.keys())

        return identifier

    def add_person(self, args):
        """
        Adds a person to the People_data dictionary 
        allocates the person to a random room.
        """

        self.person_name = args["<first_name>"] + " " + args["<last_name>"]
        message = ""
        wants_accomodation = 'N'
        is_fellow = args['Fellow']
        self.person_identifier = self.set_default_id()

        if args["<wants_accomodation>"]:
            wants_accomodation = args["<wants_accomodation>"]

        for person in people_data:
            if people_data.get(self.person_name, None) is None:
                message = "{} Already Exists".format(self.person_name)
                return message

        people_data.update({
            self.person_identifier: {
                'name': self.person_name,
                'accomodation': wants_accomodation,
                'is_fellow': is_fellow}
        })

        self.allocate_rooms(self.person_identifier)
        print rooms

        self.person_identifier += 1
        return people_data

    def allocate_rooms(self, identifier):
        """
        Checks available offices
        Checks which living spaces are available
        Randomly picks a room and appends the person identifier
        Checks if the person is a fellow and wants accomodation

        """

        available_living_spaces = []
        available_offices = []
        import ipdb
        ipdb.set_trace()

        for room in rooms:
            if rooms[room]['is_office'] and len(rooms[room]['occupants']) < 4:
                available_offices.append(room)
            elif len(rooms[room]['occupants']) < 6:
                available_living_spaces.append(room)

        if len(available_offices) > 0:
            allocated_office = random.choice(available_offices)
            rooms[allocated_office]['occupants'].append(identifier)

        if people_data[identifier]['is_fellow'] and len(available_living_spaces) > 0:
            allocated_living_space = random.choice(available_living_spaces)
            rooms[allocated_living_space]['occupants'].append(identifier)

        return rooms

    def reallocate_person(self, args):
        """
        Deletes the person identifier in the current room
        and appends it to the new room
        """

        person_identifier = int(args["<person_identifier>"])
        new_room = args["<new_room_name>"]

        for identifier in people_data["Staff"].keys():
            if identifier is person_identifier:
                name = people_data["Staff"][person_identifier]["name"]
            else:
                name = people_data["Fellow"][person_identifier]["name"]

        # find currently allocated room and remove identifier
        for current_room in rooms['Office'].keys():
            if person_identifier in rooms['Office'][current_room]:
                rooms['Office'][current_room].remove(person_identifier)
        else:
            for current_room in rooms['LivingSpace'].keys():
                if person_identifier in rooms['LivingSpace'][current_room]:
                    rooms['LivingSpace'][current_room].remove(
                        person_identifier)

        # Append identifier to new_room
        if new_room in rooms['LivingSpace'].keys():
            rooms['LivingSpace'][new_room].append(person_identifier)
        elif new_room in rooms['Office'].keys():
            rooms['Office'][new_room].append(person_identifier)

        name = name.upper()
        print name + " has been removed from " + current_room +\
            " and has been allocated to " + new_room

        return rooms

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
        with open(args["<filename>"], 'r') as input_file:
            people = input_file.readlines()
            for person in people:
                person = person.split()
                if person:
                    if 'STAFF' in person:
                        is_staff = True
                        is_fellow = False
                    else:
                        is_staff = False
                        is_fellow = True

                    if 'Y' in person:
                        wants_accomodation = 'Y'
                    else:
                        wants_accomodation = None

                    arg_dict.update({
                        "<first_name>": person[0],
                        "<last_name>": person[1],
                        "Staff": is_staff,
                        "Fellow": is_fellow,
                        "<wants_accomodation>": wants_accomodation
                    })

                    self.add_person(arg_dict)
