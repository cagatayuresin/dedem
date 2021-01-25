import wikipedia


def wikigetir(s):
    """

    :param s:
    :return:
    """
    wikipedia.set_lang("tr")
    a = str(s)
    arama = wikipedia.search(a)
    sonuc = wikipedia.page(arama[0])
    baslik = sonuc.title
    sonuclink = sonuc.url
    ozet = wikipedia.summary(baslik, chars=250)
    donut = [baslik, ozet, sonuclink]
    return donut
