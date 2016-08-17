class Person(object):
    """
    Person Class
    """

    def __init__(self):
        self.person_name = []
        self.person_identifier = 1
        self.people_data = {}
        self.staff_data = {}
        self.fellow_data = {}

    wants_accomodation = 'N'

    def add_person(self, args):
        """Adds a person to the system and allocates the person to a random room."""
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
        self.person_identifier += 1
        print self.people_data

    def load_people(self):
        pass
