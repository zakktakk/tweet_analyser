# -*- coding: utf-8 -*-
import argparse
import os
from gensim.models import word2vec
import sys
import MeCab
import numpy as np
from stopword import stopword_w2v

class W2V:
    def __init__(self, file_path):
        self.make_model(file_path)

    def make_model(self, file_path):
        data = word2vec.Text8Corpus(file_path)
        self.model = word2vec.Word2Vec(data, size=200)

    def get_topk(self, keyword, k):
        out = np.array(self.model.most_similar(positive=[keyword], topn=1000))
        result = self.get_token_list(out, k)
        return result

    def get_token_list(self, out, k):
        out = np.array(stopword_w2v(out))
        text = " ".join(out[:,0])
        token_lst = []
        pos = [u'名詞',u'動詞',u'形容詞',u'副詞',u'形容動詞']
        tagger = MeCab.Tagger("-Ochasen")
        tagger.parse('')
        node = tagger.parseToNode(text)
        count = 0
        current_pos = 0
        while node:
            if count >= k:
                break
            feature = node.feature.split(',')
            if feature[0] in pos:
                count += 1
                try:
                    token_lst.append(out[current_pos-1])
                except:
                    print('Oops!, Error occured: ' + str(node.surface))
            node = node.next
            current_pos += 1
        return token_lst


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('file_name', help='input file name',
                        type=str)
    args = parser.parse_args(arguments)
    w2v = W2V(args.file_name)
    result = w2v.get_topk("スマホ", 300)
    for word,val in result:
        print(word, val)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
