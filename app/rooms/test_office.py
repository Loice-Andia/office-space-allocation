import unittest
from officeClass import Office


class TestOffice(unittest.TestCase):
    """

    This is Test class for Office class and
    tests its initialiation

    """

    def setUp(self):
        self.test_office = Office()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_office, Office, msg="Cannot create `Office` instance")
