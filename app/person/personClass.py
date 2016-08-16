class Person(object):
    """
    Person Class
    """

    def __init__(self):
        self.person_name = []
        self.person_identifier = id(self)

    wants_accomodation = 'N'

    def add_person(self, args):
    	"""Adds a person to the system and allocates the person to a random room."""
    	self.person_name = args["<first_name>"] + " " + args["<last_name>"]
        self.wants_accomodation = args["<wants_accomodation>"]


    def load_people(self):
        pass
