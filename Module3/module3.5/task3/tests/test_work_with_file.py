import unittest
import os

from main import app


class TestWorkWithFile(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.base_url = "/file/"
        self.app = app.test_client()

        self.test_file_path = "tests/test_file.txt"
        self.wrong_test_file_path = "test_file.txt"
        self.empty_test_file_path = "empty_test_file.txt"
        self.binary_test_file_path = "binary_test_file.bin"

        with open(file=self.test_file_path, mode="w", encoding="utf-8") as test_file:
            test_file.write("tests data")

        with open(file=self.empty_test_file_path, mode="w", encoding="utf-8") as empty_test_file:
            pass

        with open(file=self.binary_test_file_path, mode="wb") as binary_test_file:
            binary_test_file.write(b"\x00\x01\x02\x03\x04\x05")

    def tearDown(self):
        os.remove(path=self.test_file_path)
        os.remove(path=self.binary_test_file_path)
        os.remove(path=self.empty_test_file_path)

    def test_file_not_exist(self):
        response = self.app.get(self.base_url + self.wrong_test_file_path)
        self.assertEqual(404, response.status_code)

    def test_file_not_empty(self):
        response = self.app.get(self.base_url + self.empty_test_file_path)
        response_text = response.data.decode()
        expected_result = "Empty"

        self.assertTrue(expected_result in response_text)

    def test_file_not_binary(self):
        with self.assertRaises(ValueError):
            self.app.get(self.base_url + self.binary_test_file_path)
