#!/bin/sh
# 
# usage : ./preprocessing.sh input_file output_file
# input : 1 tweet 1 row text file
# output : wakachigaki text file(for word2vec)

WAKATI_FILE="./wakati/"
ORIGINAL_FILE="./original_data/"

if [ $# -ne 1 ]; then
  echo "you have to input file_name"
  exit 1
fi

python drip_txt_from_tsv.py $1".tsv"
mecab ${ORIGINAL_FILE}$1".txt" -F"%f[6] " -U"%m " -E"\n" -o ${WAKATI_FILE}$1".txt"
python preprocessing.py $1".txt"
