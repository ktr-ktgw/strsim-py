# strsim-py
string similarity algorithms for unicode text


### preparation
```shell
pip install -r requirements.txt

### for using METEOR metric
python
>>> import nltk
>>> nltk.download('wordnet')
>>> nltk.download('omw-1.4')
```

### how to use
```shell
$ python strsim-py.py --help                    
usage: calculate string similarity between 2 documents

optional arguments:
  -h, --help            show this help message and exit
  --file1 FILE1         input file1
  --file2 FILE2         input file2
  -o [OUT], --out [OUT]
  -m {levenshtein,hamming,jaro,wer,ter,meteor,bleu}, --metrics {levenshtein,hamming,jaro,wer,ter,meteor,bleu}
                        sentence similarity/distance metric
  -t {no-tokenize,ja-ipadic}, --tokenize {no-tokenize,ja-ipadic}
```
- 行単位で文の 類似度/距離 を測定したいファイルを `--file1`, `--file2` から読み込む
- 類似度/距離 として使用する指標を `--metrics` オプションで指定
- 測定前処理としての分割方法を `--tokenize` で指定する。デフォルトでは入力そのまま。


### tests
```shell
python -m unittest discover tests
```