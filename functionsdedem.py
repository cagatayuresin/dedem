import datetime
import ast
import re

def kutu(name, servername, posta):
    f = open ("Others/posta.txt", "a")
    gonderi = datetime.datetime.now().strftime("\n\n%d-%m-%Y %H:%M:%S ")+servername+" "+name+"\n"+posta
    f.write(gonderi)
    f.close()
    return True

def listToString(s):
	str1 = "\n:ballot_box_with_check: ".join(str(e) for e in s)
	return str1

def log(name, command, servername, channelname):
    f = open ("Others/logs.txt", "a")
    log = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S\t")+servername+"\t"+channelname+"\t"+name+"\t"+command+"\n"
    print(log)
    f.write(log)
    f.close()
    return log

def donusturucu(isim):
    isim = str(isim)
    isim = isim.lower()
    degistir = str.maketrans("çğıöşüéä", "cgiosuea")
    isim = isim.translate(degistir)
    isim = re.sub(' +', ' ',isim)
    isim = isim.translate({ord(i): None for i in ".,:;-·''[](){}%*=&$#"})
    if isim != None:
        return isim
    else:
        return "ü"

def sansur(kelime):
    sonuc = ""
    sayi = len(kelime)
    harfler = list(kelime)
    for i in range(sayi):
        if harfler[i] != " ":
            sonuc = sonuc + "-"
        else:
            sonuc = sonuc + " "
    return sonuc
