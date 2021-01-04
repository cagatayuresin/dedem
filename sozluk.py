from tdk import tdk
from functionsdedem import *


def sozlukte(s):
    s = s.lower()
    word = tdk.new_word(s)
    listesi = word.meaning()
    sonuc = listtostring(listesi)
    return sonuc
