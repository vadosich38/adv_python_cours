import unittest

from main import app


class TestHelloUser(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello/"

    def test_can_get_user_name_in_response(self):
        user_name = "username"
        response = self.app.get(self.base_url + user_name)
        response_text = response.data.decode()

        self.assertTrue(user_name in response_text)

    def test_cannot_name_longer_15_symbols_accept(self):
        user_name = "ValentiniusKropoviy12222352d"

        with self.assertRaises(ValueError):
            self.app.get(self.base_url + user_name)

    def test_cannot_name_and_surname_accept(self):
        user_name = "Vlad Sakhabutdinov"

        with self.assertRaises(ValueError):
            self.app.get(self.base_url + user_name)
