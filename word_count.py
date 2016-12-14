# -*- coding: utf-8 -*-
"""
usage : tweet file must be wakachigakied(separated by space) & remove stop word
"""
import argparse
from itertools import chain
import sys

class WordCount:
    def __init__(self, file_path):
        self.all_tweets = self.read_file(file_path)
        self.vocabrary = list(set(chain.from_iterable(self.all_tweets[:])))

    def read_file(self, file_path):
        all_tweets = []
        with open(file_path, "r") as r_f:
            for line in r_f:
                words = line.rstrip().split()
                all_tweets.append(words)
        return all_tweets

    def get_topk(self, keyword, k):
        #if there are no match word
        if not(keyword in self.vocabrary):
            return []
        #else
        count_dict = self.make_count_dict()
        for tweet in self.all_tweets:
            if keyword in tweet:
                for word in tweet:
                    count_dict[word] += 1
        count_dict[keyword] = 0
        count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        return count_dict[:k]

    def make_count_dict(self):
        count_dict = {}
        for word in self.vocabrary:
            count_dict[word] = 0
        return count_dict


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter
                                    )
    parser.add_argument("path_to_tweet", help="path to tweet txt", type=str)
    args = parser.parse_args(arguments)
    wc = WordCount(args.path_to_tweet)
    result = wc.get_topk("スマホ", 300)
    print("word", "count")
    for i in result:
        print(i[0], i[1])
    print()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
