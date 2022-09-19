# Sentence METEOR
# nltk のライブラリの meteor_score を呼ぶだけ

from nltk.translate.meteor_score import meteor_score

def sentence_meteor(text1: str, text2: str) -> float:
    return meteor_score([text1.split()], text2.split())

