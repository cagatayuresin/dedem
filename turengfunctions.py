from tureng import TurEng
tureng = TurEng()

def ingilizceturkce(s):
    sonuc = tureng.translate(str(s))
    donutlist = sonuc.all_tr_translation_str
    donut = list(dict.fromkeys(donutlist))
    cevap = ' :white_small_square: '.join([str(elem) for elem in donut])
    return cevap

def turkceingilizce(s):
    sonuc = tureng.translate(str(s))
    donutlist = sonuc.all_en_translation_str
    donut = list(dict.fromkeys(donutlist))
    cevap = ':white_small_square:'.join([str(elem) for elem in donut])
    return cevap
