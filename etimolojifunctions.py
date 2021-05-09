import requests
from functionsdedem import listtostring
from bs4 import BeautifulSoup as bs

'''url = "https://www.nisanyansozluk.com/?k=bardak"

r = requests.get(url)
soup = bs(r.content, "html.parser")
gelen_veri = soup.find_all("tr", {"class":"yaz hghlght"})

tanim = soup.find("meta",  property="og:description")
tanim2 = tanim["content"] if title else "Özet verilmemiş.")

gelen_veri2 = gelen_veri[0].contents
gelen_veri2 = gelen_veri2[3].find_all("div", {"class":"eskoken"})

for i in range(len(gelen_veri2)):
    print(gelen_veri2[i].text)
'''
def etimoloji(sozcuk):
    url = "https://www.nisanyansozluk.com/?k=" + sozcuk
    r = requests.get(url)
    soup = bs(r.content, "html.parser")
    gelen_veri = soup.find_all("tr", {"class": "yaz hghlght"})

    tanim = soup.find("meta", property="og:description")
    tanim2 = tanim["content"] if tanim else "Özet verilmemiş."

    gelen_veri2 = gelen_veri[0].contents
    gelen_veri2 = gelen_veri2[3].find_all("div", {"class": "eskoken"})

    cevap = [tanim2]

    for i in range(len(gelen_veri2)):
        cevap.append(gelen_veri2[i].text)

    sonuc = listtostring(cevap)
    return sonuc
