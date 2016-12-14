# -*- coding: utf-8 -*-
"""
last update 12/14/2016
author : zakktakk
usage : python word_tfidf.py input_file_name keyword topk
input : wakati file (only contain specific pos words)
output : top k frequent words
example : python word_tfidf.py dripped_wakati/smaho.txt スマホ 50
"""

import argparse
import os
from itertools import chain
import collections
import sys
import math
import numpy as np

class Tfidf:
    def __init__(self, file_path):
        self.all_doc_num = 0
        self.all_tweets = list(chain.from_iterable(self.read_file(file_path)))
        self.vocabrary = list(set(self.all_tweets[:]))
        path = file_path.split("/")
        dir = "./"+"/".join(path[:len(path)-1])
        self.random_tweets = np.array(list(chain.from_iterable(self.read_file(dir+"/random.txt"))))
        self.term_frequency()
        self.document_frequency()
        self.tfidf()

    """
    def read_files(self, file_path):
        all_tweets = {}
        path = file_name.split("/")
        self.target_file = path[-1]
        dir = "./"+"/".join(path[:len(path)-1])
        files = os.listdir(dir)
        for file in files:
            root, ext = os.path.splitext(file)
            if ext == ".txt":
                tweets = []
                with open(file, "r") as r_f:
                    words = line.rstrip().split()
                    tweets.append(words)
                if file == self.target_file:
                    tweets = list(chain.from_iterable(tweets))
                all_tweets[root] = tweets
        return all_tweets
    """

    def read_file(self, file_path):
        all_tweets = []
        with open(file_path, "r") as r_f:
            for line in r_f:
                words = line.rstrip().split()
                all_tweets.append(words)
        self.all_doc_num += len(all_tweets)
        return all_tweets

    def term_frequency(self):
        self.tf = collections.Counter(self.all_tweets)
    
    def document_frequency(self):
        self.df = {}
        for word in self.vocabrary:
            self.df[word] = len(self.random_tweets[self.random_tweets == word])

    def tfidf(self):
        self.tfidf = {}
        for word, val in self.tf.items():
            if self.df[word] == 0:
                self.tfidf[word] = 0
            else:
                idf = 1 + math.log(self.all_doc_num / self.df[word])
                self.tfidf[word] = val / idf
        self.tfidf = sorted(self.tfidf.items(), key=lambda x: x[1], reverse=True)

    def get_top_k(self, k):
        return self.tfidf[:k]
        

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument("file_path", help="path to tweet text", type=str)
    parser.add_argument('topk', help='number of output word list',
                        type=str)
    args = parser.parse_args(arguments)
    result = Tfidf(args.file_path).get_top_k(int(args.topk))
    print("word", "count")
    for i in result:
        print(i[0], i[1])

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
