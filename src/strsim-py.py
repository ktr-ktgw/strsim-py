import sys
import argparse
from levenshtein import levenshtein_distance
from hamming import hamming_distance
from jaro_winkler import jaro_similarity
from meteor import sentence_meteor
from bleu import sentence_bleu
from ter import sentence_ter

import jiwer
import MeCab
import ipadic

class Sentence:
    ja_tokenizer = MeCab.Tagger(f'-O wakati {ipadic.MECAB_ARGS}')

    @staticmethod
    def notokenize(text: str) -> str:
        return text

    @staticmethod
    def tokenize_ja_ipa(text: str) -> str:
        return Sentence.ja_tokenizer.parse(text)

METRICS = {
    "levenshtein": levenshtein_distance,
    "hamming": hamming_distance,
    "jaro": jaro_similarity,
    "wer": jiwer.wer,
    "ter": sentence_ter,
    "meteor": sentence_meteor,
    "bleu": sentence_bleu,
}
TOKENIZE = {
    "no-tokenize": Sentence.notokenize,
    "ja-ipadic": Sentence.tokenize_ja_ipa,
}


def main(opt):
    calc_strsim = METRICS[opt.metrics]
    tokenize = TOKENIZE[opt.tokenize]
    with opt.file1 as fin1, opt.file2 as fin2:
        for line1 in fin1:
            line2 = fin2.readline()
            line_sim = calc_strsim(tokenize(line1), tokenize(line2))
            opt.out.write(f"{line_sim}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="calculate string similarity between 2 documents")
    parser.add_argument("--file1", type=argparse.FileType('r'), help="input file1")
    parser.add_argument("--file2", type=argparse.FileType('r'), help="input file2")
    parser.add_argument("-o", "--out", nargs="?", type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument("-m", "--metrics", type=str, choices=METRICS.keys(), help="sentence similarity/distance metric")
    parser.add_argument("-t", "--tokenize", type=str, choices=TOKENIZE.keys(), default="no-tokenize")
    #parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()
    main(args)

