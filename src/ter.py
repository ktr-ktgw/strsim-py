import sacrebleu

def sentence_ter(text1: str, text2: str) -> float:
    ter_output = sacrebleu.sentence_ter(text1, [text2])
    return ter_output.score
