import unittest
from src.bert_score_f1 import bert_score_f1


class TestBertScore(unittest.TestCase):

    def test_bert_score_ja(self):
        score_similar = bert_score_f1("大きなのっぽの古時計", "大きな古時計", "ja")
        score_different = bert_score_f1("大きな戦車", "大きな古時計", "ja")
        self.assertGreater(score_similar, score_different)


if __name__ == '__main__':
    unittest.main()