import random
import unittest

from main import app
from datetime import datetime
from freezegun import freeze_time


class TestHelloUsername(unittest.TestCase):
    dates = ["2024-03-18", "2024-03-19", "2024-03-20", "2024-03-21", "2024-03-22", "2024-03-23", "2024-03-24"]

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello/"

    @freeze_time(random.choice(dates))
    def test_day_is_right(self):
        today = datetime.today().weekday()
        days = ("понедельника", "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья")
        username = "doesntmatter"

        result = self.app.get(self.base_url + username).data.decode()
        self.assertIn(days[today], result)

    def test_username_isnt_wish(self):
        username = "Хорошей субботы!"
        with self.assertRaises(ValueError):
            self.app.get(self.base_url + username)
