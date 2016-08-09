import unittest

from app.amity.amityClass import Amity
from app.person.fellowClass import Fellow
from app.person.personClass import Person
from app.person.staffClass import Staff
from app.rooms.livingspaceClass import LivingSpace
from app.rooms.officeClass import Office
from app.rooms.roomClass import Room


class TestClasses(unittest.TestCase):
    """Class to test class initialization"""

    def setUp(self):
        self.test_amity = Amity([])
        self.test_fellow = Fellow("fellow", "Narnia", "Emerald")
        self.test_staff = Staff("staff", "Narnia")
        self.test_person = Person(1, "Emerald")
        self.test_room = Room("Emerald", "office")
        self.test_office = Office(4, 2)
        self.test_livingspace = LivingSpace(6, 2)

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_amity, Amity, msg="Cannot create `Amity` instance")
        self.assertIsInstance(
            self.test_livingspace, LivingSpace,
            msg="Cannot create `LivingSpace` instance")
        self.assertIsInstance(
            self.test_office, Office, msg="Cannot create `Office` instance")
        self.assertIsInstance(
            self.test_room, Room, msg="Cannot create `Room` instance")
        self.assertIsInstance(
            self.test_fellow, Fellow, msg="Cannot create `Fellow` instance")
        self.assertIsInstance(
            self.test_person, Person, msg="Cannot create `Person` instance")
        self.assertIsInstance(
            self.test_staff, Staff, msg="Cannot create `Staff` instance")


if __name__ == '__main__':
    unittest.main()
