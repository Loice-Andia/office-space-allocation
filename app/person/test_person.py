import unittest

from personClass import Person, people_data
from app.amity.amityClass import Amity
from fellowClass import Fellow
from staffClass import Staff


class TestPerson(unittest.TestCase):
    """

    This is Test class for Person class and its methods.
    It contains tests for the add_person, allocate_rooms, load_people,
    reallocate_person and remove_person methods.

    """

    def setUp(self):
        self.test_amity = Amity()
        self.test_fellow = Fellow()
        self.test_staff = Staff()
        self.test_person = Person()

        # Test add person function in Person class without rooms
        sample_person = {"<first_name>": "Loice",
                         "<last_name>": "Andia",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.test_person.add_person(sample_person)

        # Test loading of people from a text file
        self.test_person.load_people({"<filename>": "try.txt"})

        # Test if a person is added twice
        self.test_adding_person_twice = self.test_person.add_person(
            sample_person)

        # Test for creation of a single room
        self.test_amity.create_room(
            {"<room_name>": ["Krypton"]}, "O")

        # Test add person and allocate office
        sample_staff = {"<first_name>": "John",
                        "<last_name>": "Doe",
                        "Fellow": False,
                        "Staff": True,
                        "<wants_accomodation>": None}

        self.test_allocate_office = self.test_person.add_person(sample_staff)

        # Test adding of a fellow and allocate office and living space
        self.test_amity.create_room(
            {"<room_name>": ["Ruby"]}, "L")

        sample_fellow = {"<first_name>": "Jimmy",
                         "<last_name>": "Kamau",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.test_adding_fellow = self.test_person.add_person(sample_fellow)

        # Test reallocation of rooms
        self.test_reallocate = self.test_person.reallocate_person({
            "<person_name>": "Sule",
            "<new_room_name>": "Krypton"})

        # Test Removal of a person
        self.test_removing_person = self.test_person.remove_person(
            {"<person_name>": "KELLY"})
        self.test_remove_non_existing_person = self.test_person.remove_person(
            {"<person_name>": "TRIAL"})

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_amity, Amity, msg="Cannot create `Amity` instance")
        self.assertIsInstance(
            self.test_fellow, Fellow, msg="Cannot create `Fellow` instance")
        self.assertIsInstance(
            self.test_person, Person, msg="Cannot create `Person` instance")
        self.assertIsInstance(
            self.test_staff, Staff, msg="Cannot create `Staff` instance")

    def test_add_person_in_person(self):
        self.assertDictContainsSubset({1: {
            'name': "LOICE ANDIA",
            'accomodation': 'Y',
            'is_fellow': True}}, people_data,
            msg="Person not created")

    def test_load_people_from_a_text_file(self):
        self.assertDictContainsSubset({
            2: {'name': "OLUWAFEMI SULE",
                'accomodation': 'Y',
                'is_fellow': True},
            3: {'name': "DOMINIC WALTERS",
                'accomodation': 'N',
                'is_fellow': False}
        }, people_data,
            msg="People from text file not added")

    def test_calling_add_person_twice_with_same_args(self):
        self.assertEqual(self.test_adding_person_twice,
                         "LOICE ANDIA Already Exists\n",
                         msg="Person added twice")

    def test_office_allocation_in_add_person(self):
        self.assertRaises(Exception, self.test_allocate_office,
                          msg="Person not allocated office")

    def test_allocation_of_office_and_living_space_when_adding_a_fellow(self):
        self.assertIn("RUBY", self.test_adding_fellow,
                      msg="Person not allocated Living Space")

    def test_reallocate_room(self):
        self.assertIn("allocated KRYPTON", self.test_reallocate,
                      msg="Person has not been reallocated")

    def test_removal_of_a_person(self):
        self.assertNotEqual(None,
                            self.test_removing_person,
                            msg="Person has not been deleted")
        self.assertEqual("TRIAL not found",
                         self.test_remove_non_existing_person,
                         msg="Person found")


if __name__ == '__main__':
    unittest.main()
