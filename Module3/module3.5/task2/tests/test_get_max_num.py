import unittest
from main import app


class TestGetMaxNum(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/max_number/"

    def test_biggest_num(self):
        request_data = "4/r/3/22/11/0/54"
        expected_response = "54"

        response = self.app.get(self.base_url + request_data)
        response_text = response.data.decode()

        self.assertTrue(expected_response in response_text)

    def test_cannot_from_letters_choose(self):
        request_data = "d/d/q/w/r/-/!/a"

        with self.assertRaises(TypeError):
            self.app.get(self.base_url + request_data)
