import unittest
from main import app


class TestMoneyControl(unittest.TestCase):
    add_url = "/add/"
    calculate_url = "/calculate/"

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False

        my_app_test_client = app.test_client()

        #filling data
        my_app_test_client.get(cls.add_url + "20230101/200") #200$ за 1 января 23
        my_app_test_client.get(cls.add_url + "20240101/100") #100$ за 1 января 24

        cls.app = my_app_test_client


    #TODO: выполняется не очередно, а после test_adding
    # def test_start_data_month_calculating(self):
    #     test_datas = [("2023/01", "200"), ("2024/01", "100")]
    #
    #     for i_test_data in test_datas:
    #         with self.subTest(i_test_data=i_test_data):
    #             result = self.app.get(TestMoneyControl.calculate_url + i_test_data[0]).data.decode()
    #             self.assertIn(i_test_data[1], result)
    #
    # def test_start_data_year_calculating(self):
    #     test_datas = [("2023", "200"), ("2024", "100")]
    #
    #     for i_test_data in test_datas:
    #         with self.subTest(i_test_data=i_test_data):
    #             result = self.app.get(TestMoneyControl.calculate_url + i_test_data[0]).data.decode()
    #             self.assertIn(i_test_data[1], result)

    def test_adding(self):
        adding_data = [("20230201", "200"), ("20240201", "100"), ("20230101", "100"), ("20240101", "100")]
        expected_result = "Принята"

        for i_adding_data in adding_data:
            with self.subTest(i_adding_data=i_adding_data):
                result = self.app.get(
                    f"{TestMoneyControl.add_url}{i_adding_data[0]}/{i_adding_data[1]}").data.decode()
                self.assertIn(expected_result, result)

    def test_incorrect_date_adding(self):
        incorrect_dates = ["202401/100", "2023/100", "2412/100", "2024122/100"]

        for i_incorrect_date in incorrect_dates:
            with self.subTest(i_incorrect_date=i_incorrect_date):
                with self.assertRaises(TypeError):
                    self.app.get(TestMoneyControl.add_url + i_incorrect_date)

    def test_month_calculating(self):
        datas = [("2023/02", "200"), ("2024/02", "100"), ("2023/03", "0"),
                 ("2024/03", "0"), ("2023/01", "300"), ("2024/01", "200")]

        for i_data in datas:
            with self.subTest(i_data=i_data):
                result = self.app.get(TestMoneyControl.calculate_url + i_data[0]).data.decode()
                self.assertIn(i_data[1], result)

    def test_year_calculating(self):
        datas = [("2023", "500"), ("2024", "300"), ("2025", "0")]

        for i_data in datas:
            with self.subTest(i_data=i_data):
                result = self.app.get(TestMoneyControl.calculate_url + i_data[0]).data.decode()
                self.assertIn(i_data[1], result)

    def test_empty_month_calculating(self):
        datas = [("2021/01", "0"), ("1950", "0")]
        for i_data in datas:
            with self.subTest(i_data=i_data):
                result = self.app.get(TestMoneyControl.calculate_url + i_data[0]).data.decode()
                self.assertIn(i_data[1], result)

    def test_empty_year_calculating(self):
        datas = [("2000", "0"), ("1939", "0")]

        for i_data in datas:
            with self.subTest(i_data=i_data):
                result = self.app.get(TestMoneyControl.calculate_url + i_data[0]).data.decode()
                self.assertIn(i_data[1], result)
