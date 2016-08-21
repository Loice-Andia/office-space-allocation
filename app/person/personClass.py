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

        if args["<wants_accomodation>"] is 'Y':
            wants_accomodation = args["<wants_accomodation>"]
        elif args["<wants_accomodation>"] is None:
            wants_accomodation = 'N'

        if args["Staff"]:
            self.people_data.update({"Staff": dict([(self.person_identifier,
                                                     {'name': self.person_name, 'accomodation': wants_accomodation})])})
            self.allocate_office(self.person_identifier, self.people_data)
        elif args["Fellow"]:
            self.people_data.update({"Fellow": dict([(self.person_identifier,
                                                      {'name': self.person_name, 'accomodation': wants_accomodation})])})
            self.allocate_office(self.person_identifier, self.people_data)
            if wants_accomodation is 'Y':
                self.allocate_living_space(
                    self.person_identifier, self.people_data)

        self.person_identifier += 1

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

        return rooms

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
        print rooms
        return rooms

    def reallocate_person(self, args):
        """
        Deletes the person identifier in the current room
        and appends it to the new room
        """

        person_identifier = int(args["<person_identifier>"])
        new_room = args["<new_room_name>"]

        for identifier in self.people_data["Staff"].keys():
            if identifier is person_identifier:
                name = self.people_data["Staff"][person_identifier]["name"]
            else:
                name = self.people_data["Fellow"][person_identifier]["name"]

        print name

        # find currently allocated room
        for current_room in rooms['Office'].keys():
            if person_identifier in rooms['Office'][current_room]:
                rooms['Office'][current_room].remove(person_identifier)
        else:
            for current_room in rooms['LivingSpace'].keys():
                if person_identifier in rooms['LivingSpace'][current_room]:
                    rooms['LivingSpace'][current_room].remove(
                        person_identifier)
        print rooms
        import ipdb
        ipdb.set_trace()

        if new_room in rooms['LivingSpace'].keys():
            rooms['LivingSpace'][new_room].append(person_identifier)
        elif new_room in rooms['Office'].keys():
            rooms['Office'][new_room].append(person_identifier)

        print rooms

    def load_people(self):
        pass
