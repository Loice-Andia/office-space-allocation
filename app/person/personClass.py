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
        

    def allocate_living_space(self, identifier, data):
        # Checks if the person is a fellow and wants accomodation
        # Checks which living spaces arre available
        # Randomly picks a room and appends the person identifier
        room_list = []
        for room in rooms['LivingSpace']:
            room_list.append(room)

        allocated_room = random.choice(room_list)

        if identifier in data["Fellow"]:
            if data["Fellow"][identifier]['accomodation'] == 'Y':
                name = data["Fellow"][identifier]['name']
                print name
        import ipdb
        ipdb.set_trace()
        print allocated_room

        rooms['LivingSpace'][allocated_room].append(name)

        # if rooms['LivingSpace'][allocated_room]:
        #     rooms['LivingSpace'][allocated_room].join(identifier)

        print rooms['LivingSpace']

    def load_people(self):
        pass
