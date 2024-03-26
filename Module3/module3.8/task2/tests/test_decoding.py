import unittest
from main import decrypt


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.expected_word_result = "абра-кадабра"
        self.test_texts_to_word = ["абра-кадабра.", "абраа..-кадабра", "абраа..-.кадабра", "абра--..кадабра",
                                   "абрау...-кадабра"]

        self.test_symbols = [("абра........", ""), ("абр......a.", "a"), ("1..2.3", "23"), (".", ""),
                             ("1.......................", "")]

    def test_result_word_is_correct(self):
        for i_text in self.test_texts_to_word:
            with self.subTest(i_text=i_text):
                result = decrypt(message=i_text)
                self.assertEqual(self.expected_word_result, result)

    def test_result_symbols_is_correct(self):
        for i_symbols in self.test_symbols:
            with self.subTest(i_symbols=i_symbols):
                result = decrypt(message=i_symbols[0])
                self.assertEqual(i_symbols[1], result)


