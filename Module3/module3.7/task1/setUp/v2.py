from unittest import TestCase
from models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        #вызывается перед запуском каждого теста(функции) класса
        self.student = Student()

    def test_default_name_is_none(self):
        self.assertIsNone(self.student.name)

    def test_set_invalid_age(self):
        with self.assertRaises(ValueError):
            self.student.set_age(-100)
