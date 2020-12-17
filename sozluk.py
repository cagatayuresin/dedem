from tdk import tdk
#import requests
from functionsdedem import *

def sozlukte(s):
    s = s.lower()
    word = tdk.new_word(s)
    list = word.meaning()
    sonuc = listtostring(list)
    return sonuc
