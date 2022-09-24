import unittest
from src.sbert_cosine import sbert_cosine_score


class TestSBertCosine(unittest.TestCase):

    def test_sbert_cosine_ja(self):
        score_similar = sbert_cosine_score("これは彼の十八番の技です", "これは彼の得意な技です", "ja")
        score_different = sbert_cosine_score("これは彼の十八番の技です", "これは彼の2022番の技です", "ja")
        self.assertGreater(score_similar, score_different)


if __name__ == '__main__':
    unittest.main()