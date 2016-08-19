import random
from app.amity.amityClass import rooms


class Person(object):
    """
    Person Class
    """

    def __init__(self):
        self.person_name = []
        self.person_identifier = 1
        self.people_data = {}

    wants_accomodation = 'N'

    def add_person(self, args):
        """
        Adds a person to the system and allocates the person to a random room.
        """

        self.person_name = args["<first_name>"] + " " + args["<last_name>"]

        if args["<wants_accomodation>"] == 'Y':
            wants_accomodation = args["<wants_accomodation>"]
        elif args["<wants_accomodation>"] == 'N' or args["Staff"]:
            wants_accomodation = 'N'

        if args["Staff"]:
            self.people_data.update({"Staff": dict([(self.person_identifier,
                                                     {'name': self.person_name, 'accomodation': wants_accomodation})])})
            self.allocate_office(self.person_identifier, self.people_data)
        elif args["Fellow"]:
            self.people_data.update({"Fellow": dict([(self.person_identifier,
                                                      {'name': self.person_name, 'accomodation': wants_accomodation})])})
            self.allocate_office(self.person_identifier, self.people_data)
            self.allocate_living_space(
                self.person_identifier, self.people_data)

        self.person_identifier += 1

    def allocate_living_space(self, identifier, data):
        # Checks if the person is a fellow and wants accomodation
        # Checks which living spaces arre available
        # Randomly picks a room and appends the person identifier
        available_living_spaces = []

        for room in rooms['LivingSpace']:
            if len(rooms['LivingSpace'][room]) < 6:
                available_living_spaces.append(room)

        allocated_living_space = random.choice(available_living_spaces)

        rooms['LivingSpace'][allocated_living_space].append(identifier)

        return rooms

    def allocate_office(self, identifier, data):
        # Randomly picks an office and appends the person identifier
        available_offices = []

        for office in rooms['Office']:
            if len(rooms['Office'][office]) < 4:
                available_offices.append(office)

        allocated_office = random.choice(available_offices)
        # print rooms
        rooms['Office'][allocated_office].append(identifier)
        return rooms

    def load_people(self):
        pass
