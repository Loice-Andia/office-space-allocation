import random
from app.amity.amityClass import rooms

people_data = {}


class Person(object):
    """
    Person Class
    """

    def __init__(self):
        self.person_name = []
        self.person_identifier = 1

    wants_accomodation = 'N'

    def add_person(self, args):
        """
        Adds a person to the system and allocates the person to a random room.
        """

        self.person_name = args["<first_name>"] + " " + args["<last_name>"]

        if args["<wants_accomodation>"] is 'Y':
            wants_accomodation = args["<wants_accomodation>"]
        elif args["<wants_accomodation>"] is None:
            wants_accomodation = 'N'

        if args["Staff"]:
            people_data.update({
                "Staff": dict([(self.person_identifier,
                                {'name': self.person_name, 'accomodation': wants_accomodation})])
            })
            office = self.allocate_office(self.person_identifier, people_data)
        elif args["Fellow"]:
            people_data.update({
                "Fellow": dict([(self.person_identifier,
                                 {'name': self.person_name, 'accomodation': wants_accomodation})])
            })
            office = self.allocate_office(self.person_identifier, people_data)
            livingspace = ""
            if wants_accomodation is 'Y':
                livingspace = self.allocate_living_space(
                    self.person_identifier, people_data)
        print self.person_name.upper() + " has been allocated "\
            + office.upper() + " office."
        if livingspace != "":
            print self.person_name.upper() + " has been allocated "\
                + livingspace.upper() + " Living Space."
        else:
            print "No living Space allocated"

        self.person_identifier += 1
        return people_data

    def allocate_living_space(self, identifier, data):
        """
        Checks if the person is a fellow and wants accomodation
        Checks which living spaces are available
        Randomly picks a room and appends the person identifier

        """

        available_living_spaces = []

        for room in rooms['LivingSpace']:
            if len(rooms['LivingSpace'][room]) < 6:
                available_living_spaces.append(room)

        allocated_living_space = random.choice(available_living_spaces)

        rooms['LivingSpace'][allocated_living_space].append(identifier)

        return allocated_living_space

    def allocate_office(self, identifier, data):
        """
        Checks which offices are available
        Randomly picks an office and appends the person identifier
        """
        available_offices = []

        for office in rooms['Office']:
            if len(rooms['Office'][office]) < 4:
                available_offices.append(office)

        allocated_office = random.choice(available_offices)
        # print rooms
        rooms['Office'][allocated_office].append(identifier)

        return allocated_office

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
                # import ipdb
                # ipdb.set_trace()

                if person:
                    if person[2] is 'STAFF':
                        is_staff = True
                        is_fellow = False
                    else:
                        is_staff = False
                        is_fellow = True

                    if len(person) is 4:
                        if person[3] is 'Y':
                            wants_accomodation = person[3]
                        elif person[3] is 'N':
                            wants_accomodation = None
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
