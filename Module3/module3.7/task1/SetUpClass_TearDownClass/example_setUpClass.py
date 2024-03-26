from unittest import TestCase
from hello_word_with_day import app


class TestHelloWorldWithDayApp(TestCase):
    @classmethod
    def setUpClass(cls):
        #выполняется перед запуском всех тестов данного класса
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url: str = '/hello-world/'

    def test_can_get_correct_username_with_weekdate(self):
        username: str = 'username'
        response = self.app.get(self.base_url + username)
        response_text: str = response.data.decode()
        self.assertIn(username, response_text)