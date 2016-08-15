class Person(object):
    """
    Person Class
    """

    def __init__(self, person_identifier, person_name):
        self.person_name = person_name
        self.person_identifier = person_identifier

    wants_accomodation = 'N'

    def add_person(self, person_role, wants_accomodation):
    	"""Adds a person to the system and allocates the person to a random room."""
    	
        self.person_role = person_role
        self.wants_accomodation = wants_accomodation


    def load_people(self):
        pass
