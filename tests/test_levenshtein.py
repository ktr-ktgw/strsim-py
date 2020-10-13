import unittest
from src.levenshtein import levenshtein_distance

class TestLevenshtein(unittest.TestCase):

    def test_levenshtein_equal(self):
        self.assertEqual(levenshtein_distance('hoge', 'hoge'), 0)
        self.assertEqual(levenshtein_distance('あ亜', 'あ亜'), 0)

    def test_levenshtein_diff(self):
        self.assertEqual(levenshtein_distance('hoge', 'fuga'), 3)
        self.assertEqual(levenshtein_distance('琴稲妻', '琴光喜'), 2)
        self.assertEqual(levenshtein_distance('hogefuga', 'huga'), 4)
        self.assertEqual(levenshtein_distance('これはこれはすばらしい', 'これなんだい'), 8)


if __name__ == '__main__':
    unittest.main()