class Amity(object):
    """Super class for amity"""

    def __init__(self, rooms=[]):
        super(Amity, self).__init__()
        self.rooms = rooms

    def create_room(self, room_name):
        self.room_name = room_name
        self.rooms.append(self.room_name)

    def save_state(self):
        pass

    def load_state(self):
        pass
