class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        self.rooms = []

    def create_room(self, args):
        for room in args["<room_name>"]:
            # print room
            self.rooms.append(room)
        print self.rooms

    def save_state(self):
        pass

    def load_state(self):
        pass
