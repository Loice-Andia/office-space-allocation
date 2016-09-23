import unittest
import mock
from personClass import Person


class TestPerson(unittest.TestCase):
    """

    This is Test class for Person class and its methods.
    It contains tests for the add_person, allocate_rooms, load_people,
    reallocate_person and remove_person methods.

    """

    def setUp(self):
        self.test_person = Person()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_person, Person, msg="Cannot create `Person` instance")

    def test_add_person_in_person(self):
        # Test add person function in Person class without rooms
        sample_person = {"<first_name>": "Loice",
                         "<last_name>": "Andia",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        add_person = self.test_person.add_person(sample_person)
        add_person_twice = self.test_person.add_person(sample_person)
        self.assertIn('LOICE ANDIA', add_person,
                      msg="Person not created")
        self.assertEqual(add_person_twice,
                         "LOICE ANDIA Already Exists\n",
                         msg="Person added twice")

    @mock.patch('personClass.open')
    @mock.patch('personClass.Person.add_person')
    def test_load_people_from_a_text_file(self, mocked_add_person, mocked_open):

        self.test_person.load_people({"<filename>": "non_existent.txt"})
        mocked_open.assert_called_once_with("non_existent.txt", 'r')

        sample_txt_data = "OLUWAFEMI SULE FELLOW Y\nDOMINIC WALTERS STAFF\nSIMON PATTERSON FELLOW Y\n"

        with mock.patch('builtins.open', mock.mock_open(read_data=sample_txt_data)) as mock_file:
            mock_read_line = open("try.txt").readline()
            assert mock_file.called
        mock_file.assert_called_once_with("try.txt")
        self.assertEqual(mock_read_line, "OLUWAFEMI SULE FELLOW Y\n")

        mocked_add_person.return_value = "OLUWAFEMI SULE has been allocated No office and No livingSpace\n"
        self.assertEqual("OLUWAFEMI SULE has been allocated No office and No livingSpace\n",
                         mocked_add_person.return_value, msg="Person not added from file")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': []}})
    def test_office_allocation_in_add_person(self):

        # Test add person and allocate office
        sample_staff = {"<first_name>": "John",
                        "<last_name>": "Doe",
                        "Fellow": False,
                        "Staff": True,
                        "<wants_accomodation>": None}

        self.test_allocate_office = self.test_person.add_person(sample_staff)
        self.assertRaises(Exception, self.test_allocate_office,
                          msg="Person not allocated office")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': []},
        'RUBY': {'is_office': False, 'occupants': []}})
    def test_allocation_of_office_and_living_space_when_adding_a_fellow(self):
        # Test adding of a fellow and allocate office and living space
        sample_fellow = {"<first_name>": "Jimmy",
                         "<last_name>": "Kamau",
                         "Fellow": True,
                         "Staff": False,
                         "<wants_accomodation>": 'Y'}

        self.adding_fellow = self.test_person.add_person(sample_fellow)
        self.assertIn("RUBY", self.adding_fellow,
                      msg="Person not allocated Living Space")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': []},
        'VALHALLA': {'is_office': True, 'occupants': [1]},
        'JADE': {'is_office': False, 'occupants': [1]},
        'EMERALD': {'is_office': False, 'occupants': [5]},
        'OCULUS': {'is_office': True, 'occupants': [2, 3, 4, 5]}})
    @mock.patch.dict('personClass.people_data', {
        1: {'name': 'OLUWAFEMI SULE', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'NJIRA PERCI', 'is_fellow': False, 'accomodation': 'N'}})
    def test_reallocate_room(self):
        # Test reallocation of rooms
        self.reallocate = self.test_person.reallocate_person({
            "<person_name>": "Sule",
            "<new_room_name>": "Krypton"})
        self.assertIn("allocated KRYPTON", self.reallocate,
                      msg="Person has not been reallocated")

        self.reallocate_to_full_room = self.test_person.reallocate_person({
            "<person_name>": "Sule",
            "<new_room_name>": "oculus"})
        self.assertIn("full", self.reallocate_to_full_room,
                      msg="Person has not been reallocated")

        self.reallocate_staff_living_space = self.test_person.reallocate_person({
            "<person_name>": "Njira",
            "<new_room_name>": "jade"})
        self.assertEqual(self.reallocate_staff_living_space,
                         "STAFF CANNOT BE ALLOCATED LIVING SPACES",
                         msg="Staff allocated living spaces")

        self.reallocate = self.test_person.reallocate_person({
            "<person_name>": "Sule",
            "<new_room_name>": "Emerald"})
        self.assertIn("allocated EMERALD", self.reallocate,
                      msg="Person has not been reallocated")

    @mock.patch.dict('personClass.people_data', {
        8: {'name': 'KELLY MCGUIRE', 'is_fellow': True, 'accomodation': 'Y'}})
    def test_removal_of_a_person(self):
        # Test Removal of a person
        self.removing_person = self.test_person.remove_person(
            {"<person_name>": "KELLY"})
        self.remove_non_existing_person = self.test_person.remove_person(
            {"<person_name>": "TRIAL"})
        self.assertNotEqual(None,
                            self.removing_person,
                            msg="Person has not been deleted")
        self.assertEqual("TRIAL not found",
                         self.remove_non_existing_person,
                         msg="Person found")


if __name__ == '__main__':
    unittest.main()
