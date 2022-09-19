import sacrebleu


def sentence_bleu(text1: str, text2: str) -> float:
    bleu_output = sacrebleu.sentence_bleu(text1, [text2], smooth_method="exp")
    return bleu_output.score
