import random
from app.amity.amityClass import Amity, rooms
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

        print args["<wants_accomodation>"]

        if args["Staff"]:
            self.people_data.update({"Staff": dict([(self.person_identifier,
                                                     {'name': self.person_name, 'accomodation': wants_accomodation})])})
        elif args["Fellow"]:
            self.people_data.update({"Fellow": dict([(self.person_identifier,
                                                      {'name': self.person_name, 'accomodation': wants_accomodation})])})

            self.allocate_living_space(
                self.person_identifier, self.people_data)

        self.person_identifier += 1
        print self.people_data

    def allocate_living_space(self, identifier, data):
        # Checks if the person is a fellow and wants accomodation
        # Checks which living spaces arre available
        # Randomly picks a room and appends the person identifier
        
        
        if identifier in data["Fellow"]:
            if data["Fellow"][identifier]['accomodation'] == 'Y':
                print rooms


    def load_people(self):
        pass
