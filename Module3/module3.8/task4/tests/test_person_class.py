import unittest
from datetime import datetime
from main import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.name1 = "Vlad"
        self.name2 = "Olya"
        self.yob = 1997
        self.old = datetime.now().year - self.yob
        self.address1 = "Schreberstr 30"
        self.address2 = "Altalmrich 33"
        self.pers_instance = Person(name=self.name1, year_of_birth=self.yob, address=self.address1)

    def test_get_name_is_correct(self):
        get_name_method_result = self.pers_instance.get_name()

        self.assertCountEqual(get_name_method_result, self.name1)

    def test_change_name(self):
        self.pers_instance.set_name(name=self.name2)
        get_name_method_result = self.pers_instance.get_name()

        self.assertEqual(get_name_method_result, self.name2)

    def test_age_is_correct(self):
        get_age_method_result = self.pers_instance.get_age()

        self.assertEqual(get_age_method_result, self.old)

    def test_address_is_correct(self):
        get_address_method_result = self.pers_instance.get_address()

        self.assertEqual(get_address_method_result, self.address1)

    def test_change_address(self):
        self.pers_instance.set_address(address=self.address2)
        get_address_method_result = self.pers_instance.get_address()

        self.assertEqual(get_address_method_result, self.address2)

    def test_is_homeless(self):
        self.assertFalse(self.pers_instance.is_homeless())
