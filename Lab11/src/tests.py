import unittest
from prefix_function import prefix_function
from kmp_search import kmp_search
from z_function import z_search
from string_matching import rabin_karp, boyer_moore

class TestStringAlgorithms(unittest.TestCase):

    def setUp(self):
        self.texts = ["abcabcabc", "aaaaaa", "abracadabra", ""]
        self.patterns = ["abc", "aa", "abra", ""]

    def test_prefix_function(self):
        self.assertEqual(
            prefix_function("abcdabca"),
            [0,0,0,0,1,2,3,1],
            "Ошибка в вычислении префикс-функции для 'abcdabca'"
        )
        print("Тест prefix_function пройден успешно")

    def test_kmp_search(self):
        self.assertEqual(kmp_search("abcabcabc", "abc"), [0,3,6])
        self.assertEqual(kmp_search("aaaaaa", "aa"), [0,1,2,3,4])
        print("Тест kmp_search пройден успешно")

    def test_z_search(self):
        self.assertEqual(z_search("abcabcabc", "abc"), [0,3,6])
        self.assertEqual(z_search("aaaaaa", "aa"), [0,1,2,3,4])
        print("Тест z_search пройден успешно")

    def test_rabin_karp(self):
        self.assertEqual(rabin_karp("abcabcabc", "abc"), [0,3,6])
        print("Тест rabin_karp пройден успешно")

    def test_boyer_moore(self):
        self.assertEqual(boyer_moore("abcabcabc", "abc"), [0,3,6])
        print("Тест boyer_moore пройден успешно")

if __name__ == "__main__":
    unittest.main()
