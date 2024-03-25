import unittest
from main import get_social_status


class TestSocialStatus(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        expected_res = "ребенок"
        func_res = get_social_status(age=age)
        self.assertEqual(expected_res, func_res)

    def test_can_get_teen_age(self):
        age = 16
        expected_res = "подросток"
        func_res = get_social_status(age=age)
        self.assertEqual(expected_res, func_res)

    def test_can_get_adult_age(self):
        age = 25
        expected_res = "взрослый"
        func_res = get_social_status(age=age)
        self.assertEqual(expected_res, func_res)

    def test_can_get_old_age(self):
        age = 60
        expected_res = "пожилой"
        func_res = get_social_status(age=age)
        self.assertEqual(expected_res, func_res)

    def test_can_get_pension_age(self):
        age = 70
        expected_res = "пенсионер"
        func_res = get_social_status(age=age)
        self.assertEqual(expected_res, func_res)

    def test_cannot_pass_str_as_age(self):
        age = "age"
        with self.assertRaises(ValueError):
            get_social_status(age=age)

    def test_cannot_pass_minus_as_age(self):
        age = -2
        with self.assertRaises(ValueError):
            get_social_status(age=age)
