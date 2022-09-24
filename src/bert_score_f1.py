from bert_score import score


def bert_score_f1(text1: str, text2: str, lang=None) -> float:
    cands = [text1]
    refs = [text2]
    precision, recall, f1 = score(cands, refs, lang=lang, verbose=True)
    return f1.tolist()[0]
