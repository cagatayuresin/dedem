import datetime
import re
import pandas as pd
import random
import wikipedia
from tureng import TurEng
from youtubepy import Video
from tdk import tdk
import imdb
import requests
from bs4 import BeautifulSoup as bs
import csv

#commander controller
def wrapper(context):
    def check_msg(message):
        return context.author == message.author and context.channel == message.channel

    return check_msg

#logger
def log(user, command, guild, channel):
    theDate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("DB/logs.txt","a", encoding="utf-8") as f:
        record = "{};{};{};{};{}\n".format(theDate, guild, channel, user, command)
        print(record)
        f.write(record)
    return record

#ballot box list maker
def listtostring(s) -> object:
    str1 = "\n:ballot_box_with_check: ".join(str(e) for e in s)
    return str1

#etymology command
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

#imdb commands
ia = imdb.IMDb()

def top250random():
    search = ia.get_top250_movies()
    film = random.choice(search)
    return film

def bottom100random():
    search = ia.get_bottom100_movies()
    film = random.choice(search)
    return film

def imdbarama(s):
    name = str(s)
    movies = ia.search_movie(name)
    return movies

def imdblinkleri(k, movies):
    resultx = ""
    for i in range(k):
        result = str(ia.get_imdbURL(movies[i]))
        resultx = resultx + "\n" + result
    return resultx

def linkinedir(s):
    a = ia.get_imdbURL(s)
    return a

def imdbpuanlari(k, movies):
    resultx = ""
    for i in range(k):
        movie = ia.get_movie(str(movies[i].movieID))
        puan = movie.get('rating')
        try:
            years = str(movies[i]['year'])
        except KeyError:
            years = "-"
        result = ":film_frames: **" + str(i+1) + "**" + " - " + "*" + movies[i]['title'] + "* (" + years + ")" + "** IMDb ID: **" + str(movies[i].movieID) + " **IMDb Puanı: **" + str(puan)
        resultx = resultx + "\n" + result
    return resultx

#wiki command
def wikigetir(s):
    wikipedia.set_lang("tr")
    a = str(s)
    arama = wikipedia.search(a)
    sonuc = wikipedia.page(arama[0])
    baslik = sonuc.title
    sonuclink = sonuc.url
    ozet = wikipedia.summary(baslik, chars=200)
    donut = [baslik, ozet, sonuclink]
    return donut

#engtur command
def ingilizceturkce(s):
    tureng = TurEng()
    sonuc = tureng.translate(str(s))
    donutlist = sonuc.all_tr_translation_str
    donut = list(dict.fromkeys(donutlist))
    cevap = ' :white_small_square: '.join([str(elem) for elem in donut])
    return cevap

#tureng command
def turkceingilizce(s):
    tureng = TurEng()
    sonuc = tureng.translate(str(s))
    donutlist = sonuc.all_en_translation_str
    donut = list(dict.fromkeys(donutlist))
    cevap = ':white_small_square:'.join([str(elem) for elem in donut])
    return cevap

"""def kutu(name, servername, gonderimetni):
    f = open("Others/posta.txt", "a")
    gonderi = datetime.datetime.now().strftime("\n\n%d-%m-%Y %H:%M:%S ") + servername + " " + name + "\n" + gonderimetni
    f.write(gonderi)
    f.close()
    return True"""

#tdk command
def sozlukte(s):
    s = s.lower()
    word = tdk.new_word(s)
    listesi = word.meaning()
    sonuc = listtostring(listesi)
    return sonuc

#adamasmaca command
def donusturucu(isim):
    isim = str(isim)
    isim = isim.lower()
    degistir = str.maketrans("çğıöşüéä", "cgiosuea")
    isim = isim.translate(degistir)
    isim = re.sub(' +', ' ', isim)
    isim = isim.translate({ord(i): None for i in ".,:;-·''[](){}%*=&$#!?"})
    if isim is not None:
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

#youtube command
def youtube_arat(s):
    tr2_eng = str.maketrans("çğıöşü", "cgiosu")
    arama = s.lower()
    arama = arama.translate(tr2_eng)
    video = Video(arama)
    sonuc = video.search()
    return sonuc

#database tools
moviesdata = pd.read_csv("DB/movies.csv", encoding="ISO-8859-1", delimiter=';')

original_title = moviesdata["original_title"]
imdb_rating = moviesdata["avg_vote"]
genres = moviesdata["genre"]
imdbid = moviesdata["imdb_title_id"]
year = moviesdata["year"]
lang = moviesdata["language"]

def get_the_year(i):
    yil = str(year[i])
    return yil

def get_the_point(i):
    puan = str(imdb_rating[i])
    return puan

def get_the_link(i):
    link = str(imdbid[i])
    link = "https://www.imdb.com/title/" + link
    return link

def get_genres(i):
    i = int(i)
    turleri = genres[i]
    turleri = turleri.split(", ")
    turleri = [item.lower() for item in turleri]
    return turleri

def getting_lang(i):
    dil = lang[i]
    return dil

def get_random_movie():
    i = random.randint(0, 2019)
    title = getting_title(i)
    dil = getting_lang(i)
    return [title, dil]

def getting_title(i):
    title = str(original_title[i])
    return title

#highscores
def getuserhs(user, guild):
    hs = pd.read_csv("DB/adamasmacahigh.csv", encoding="utf-8", delimiter=',')
    rslt_df = hs.sort_values(by = ['score'], ascending = False)
    print(rslt_df)
    users = rslt_df["user"]
    guilds = rslt_df["guild"]
    highscore = rslt_df["score"]
    list = [0]
    for i in range(len(hs)):
        if users[i] == user and guilds[i] == guild:
            list.append(int(highscore[i]))
    return list
    
    """with open('DB/adamasmacahigh.csv', newline='') as db:
        reader = csv.DictReader(db)
        for row in reader:
            print(row['first_name'], row['last_name'])
            if row['guild'] == guild and row["user"]:
                return row["score"]"""

def appendhs(user,guild,score):
    guild = guild.replace(",","")
    score= str(score)
    with open(r"DB/adamasmacahigh.csv", "a", encoding="utf-8", newline='') as db:
        fieldnames = ['user','guild', 'score']
        writer = csv.DictWriter(db, fieldnames=fieldnames)
        dict = {'user':user, 'guild': guild, 'score': score}
        writer.writerow(dict)
        #writer = csv.writer(db)
        #writer.writerow({user,guild,score})
        #writer.writerow({'user': user, 'guild': guild, 'score': score})
    return

def besths(guild):
    hs = pd.read_csv("DB/adamasmacahigh.csv", encoding="utf-8", delimiter=',')
    rslt_df = hs.sort_values(by = ['score'], ascending = False)
    print(rslt_df)
    users = rslt_df["user"]
    guilds = rslt_df["guild"]
    highscore = rslt_df["score"]
    bestperson = ["Null", "0"]
    for i in range(len(rslt_df)):
        if guilds[i] == guild and int(highscore[i])>int(bestperson[1]):
            bestperson = [users[i], highscore[i]]
    return bestperson

"""def main():
    user = input("user: ")
    guild = input("guild: ")
    #score = input("score: ")
    #appendhs(guild, user, score)
    #time.sleep(3)
    line = getuserhs(user, guild)
    print(line)

main()"""