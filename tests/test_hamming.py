import unittest
from src.hamming import hamming_distance

class TestHamming(unittest.TestCase):

    def test_hamming_equal(self):
        self.assertEqual(hamming_distance('hoge', 'hoge'), 0)
        self.assertEqual(hamming_distance('あ亜', 'あ亜'), 0)

    def test_hamming_diff(self):
        self.assertEqual(hamming_distance('hoge', 'fuga'), 3)
        self.assertEqual(hamming_distance('琴稲妻', '琴光喜'), 2)

    def test_hamming_error(self):
        with self.assertRaises(Exception):
            hamming_distance('string', 'str')


if __name__ == '__main__':
    unittest.main()