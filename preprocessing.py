# -*- coding: utf-8 -*-
import MeCab
import argparse
import sys
from stopword import stopword

WAKATI_DIR = "./wakati/"
DRIPPED_WAKATI_DIR = "./dripped_wakati/"

def get_token_list(text):
    token_lst=[]
    pos = [u'名詞',u'動詞',u'形容詞',u'副詞',u'形容動詞']
    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse('')
    node = tagger.parseToNode(text)
    while node:
        feature = node.feature.split(',')
        if feature[0] in pos:
            try:
                token_lst.append(node.surface)
            except:
                print('Oops!, Error occured: ' + str(node.surface))
        node = node.next
    return token_lst

def output_dripped_file(input_file, output_file):
    input_f = open(input_file, 'r')
    output_f = open(output_file, 'w')
    for line in input_f:
        line = line.rstrip()
        result = stopword(get_token_list(line))
        output_f.write(' '.join(result)+'\n')
    input_f.close()
    output_f.close()

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('file_name', help='input file name',
                        type=str)
    args = parser.parse_args(arguments)
    output_dripped_file(WAKATI_DIR+args.file_name, DRIPPED_WAKATI_DIR+args.file_name)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
