class Person(object):
	"""
	Person Class
	"""
	def __init__(self, person_identifier, person_name):
		self.person_name = person_name
		self.person_identifier = person_identifier

	def add_person(self, person_name, person_identifier):
		self.person_name = person_name
		self.person_identifier = person_identifier

	def load_people(self):
		pass
