# -*- coding: utf-8 -*-
import MeCab
import argparse
import sys
import pandas as pd
import numpy as np
from stopword import remove_url

TWEET_DIR = "./tweet_data/"
ORIGINAL_DIR = "./original_data/"

def output_original_file(input_file, output_file):
    with open(output_file, "w") as output_f:
        df_tweet = pd.read_csv(input_file, delimiter='\t')
        for i, row in df_tweet.iterrows():
            output_f.write(remove_url(str(row["contents"])) + "\n")

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('file_name', help='input file name',
                        type=str)
    args = parser.parse_args(arguments)
    output_original_file(TWEET_DIR+args.file_name, ORIGINAL_DIR+args.file_name.rstrip(".tsv")+".txt")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
