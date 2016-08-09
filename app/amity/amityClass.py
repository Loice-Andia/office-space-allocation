class Amity(object):
	"""Super class for amity"""
	def __init__(self, rooms):
		super(Amity, self).__init__()
		self.rooms = rooms

	def create_room(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type

	def save_state(self):
		pass

	def load_state(self):
		pass

		
