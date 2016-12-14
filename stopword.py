# -*- coding: utf-8 -*-
import re

def stopword(words):
  single = r"^[0-9０-９ぁ-んァ-ン！%％？・　!-/:-@≠\[-`{-~\u3001-\u303F]$"
  pair    = r"^[ぁ-んa-zA-Z]{2}$"
  triple    = r"^[a-zA-Z]{3}$"
  quatro    = r"^[a-zA-Z]{4}$"
  numb  =r"^[0-9]+$"  
  return [ x for x in words if len(x) > 1 and re.match( pair, x ) is None and re.match( numb, x) is None]

def stopword_w2v(pair_words):
    single = r"^[0-9０-９ぁ-んァ-ン！%％？・　!-/:-@≠\[-`{-~\u3001-\u303F]$"
    pair    = r"^[ぁ-んa-zA-Z]{2}$"
    triple    = r"^[a-zA-Z]{3}$"
    quatro    = r"^[a-zA-Z]{4}$"
    numb  =r"^[0-9]+$"  
    return [ x for x in pair_words if len(x[0]) > 1 and re.match( pair, x[0] ) is None and re.match( numb, x[0]) is None]

def remove_url(words):
    return re.sub(r'(?:^|[\s　]+)((?:https?|ftp):\/\/[^\s　]+)', "", words)
