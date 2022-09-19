import unittest
from src.jaro_winkler import jaro_similarity

class TestJaroWinkler(unittest.TestCase):

    def test_jaro_equal(self):
        self.assertEqual(jaro_similarity('hoge', 'hoge'), 1)
        self.assertEqual(jaro_similarity('あ亜', 'あ亜'), 1)

    def test_jaro_diff(self):
        self.assertEqual(round(jaro_similarity('MARTHA', 'MARHTA'), 6), 0.944444)
        self.assertEqual(round(jaro_similarity('DIXON', 'DICKSONX'), 6), 0.766667)
        self.assertEqual(jaro_similarity('MARTHA', 'hoge'), 0)


if __name__ == '__main__':
    unittest.main()