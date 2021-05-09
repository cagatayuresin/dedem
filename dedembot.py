import discord
from discord.ext import commands
from config import *
from imdbfunctions import *
from sozluk import *
from youtubearama import *
from wikipediafunctions import *
from turengfunctions import *
from datafunctions import *
from etimolojifunctions import *
import time
import random

anahtar = 1
dedembotversion = the_bot_version()
komut_onculu = the_prefix(anahtar)
client = commands.Bot(command_prefix=komut_onculu, help_command=None)


# mesaj yazarı kontrolcüsü
def wrapper(context):
    def check_msg(message):
        return context.author == message.author and context.channel == message.channel

    return check_msg


@client.event
async def on_ready():
    izliyor = komut_onculu + "yardım için"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=izliyor))
    print("Bot Hazır!")


@client.command(aliases=["türöner", "Tureoner", "Türöner"])
async def turoner(ctx, arg="empty"):
    komut = "turoner"
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    oyuncu = ctx.message.author.name
    log(oyuncu, komut, sunucu, kanaladi)
    turlistesi = ['suç', 'drama', 'korku', 'aşk', 'komedi', 'gerilim', 'biyografi', 'tarih', 'gizem', 'western', 'aile',
                  'macera', 'bilimkurgu', 'spor', 'animasyon', 'savaş', 'müzikal', 'aksiyon', 'fantastik', 'müzik',
                  'belgesel']
    turlistesiing = ['crime', 'drama', 'horror', 'romance', 'comedy', 'thriller', 'biography', 'history', 'mystery',
                     'western', 'family', 'adventure', 'sci-fi', 'sport', 'animation', 'war', 'musical', 'action',
                     'fantasy', 'music', 'documentary']
    if arg != "empty":
        kontrol = True
        istenilen_tur = arg.lower()

        if istenilen_tur in turlistesi:
            for x in range(len(turlistesi)):
                if istenilen_tur == turlistesi[x]:
                    istenilen_tur = turlistesiing[x]
                else:
                    continue
        else:
            kontrol = False
            await ctx.send("**Düzgün yazar mısın şunu!!** "+ arg +"** nedir allaşkına?**")

        while kontrol is True:
            i = random.randint(1, 2019)
            turler = get_genres(i)
            if istenilen_tur in turler:
                sonuc = getting_title(i) + " " + get_the_year(i) + " " + get_the_point(i) + "\n" + get_the_link(i)
                await ctx.send(sonuc)
                kontrol = False
            else:
                continue
    else:
        mesaj = "`" + komut_onculu + "türöner 'listeden seçin'`\n"
        turler = ""
        for ele in turlistesi:
            turler = turler + " | " + ele + " | "
        mesaj = mesaj + turler
        await ctx.send(mesaj)


@client.command(aliases=['yaklaş', 'Yaklas', 'Yaklaş'])
async def yaklas(ctx):
    komut = "yaklas"
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    oyuncu = ctx.message.author.name
    log(oyuncu, komut, sunucu, kanaladi)
    skor = 1000
    strskor = "\nSkor: "
    soru = random.randint(1, 99)
    kontrol = False
    botsorusu = "Aklımdan 0 ile 100 arasında bir sayı tuttum. Tahmin etmek ister misin?"
    bildirim = "\nOyun başladı."
    iptal = "\nÇıkmak için iptal yazabilirsin."
    botmessage = await ctx.send("```" + botsorusu + bildirim + "\n" + oyuncu + iptal + "```")
    counter = 0
    try:
        while not kontrol:
            tahmin = await client.wait_for('message', timeout=45, check=wrapper(ctx))
            counter += 1
            if tahmin.author.name == oyuncu:
                msg = tahmin
                cevap = tahmin.content
                cevap = cevap.replace("İptal", "iptal")
                cevap = cevap.lower()
                time.sleep(1)
                await msg.delete()
                if cevap == "iptal":
                    await botmessage.delete()
                    bildirim = "\nOyun iptal edildi."
                    botmessage = await ctx.send("```" + botsorusu + bildirim + "\n" + oyuncu + "```")
                    kontrol = True
                else:
                    try:
                        cevapint = int(cevap)
                        if 0 < cevapint < 100:
                            if cevapint == soru:
                                if counter == 1:
                                    bildirim = "\nLan yok artık. Tek seferde. Cevap şuydu gerçekten de: "
                                    skor = 666
                                else:
                                    bildirim = "\nValla bravo. Cevap şuydu: "
                                    skor = skor - counter * 2
                                await botmessage.delete()
                                botmessage = await ctx.send("```" + botsorusu + bildirim + str(soru) + strskor + str(skor) + "\n" + oyuncu + "```")
                                kontrol = True
                            elif cevapint < soru:
                                skor = skor - counter * 2
                                await botmessage.delete()
                                bildirim = "\nYüksek söyle."
                                botmessage = await ctx.send("```" + botsorusu + bildirim + strskor + str(skor) + "\n" + oyuncu + iptal + "```")
                            else:
                                skor = skor - counter * 2
                                await botmessage.delete()
                                bildirim = "\nDüşük söyle."
                                botmessage = await ctx.send("```" + botsorusu + bildirim + strskor + str(skor) + "\n" + oyuncu + iptal + "```")
                        else:
                            await botmessage.delete()
                            skor = skor - 300
                            bildirim = "\n1 ile 100 arasında bir sayı girmelisin."
                            botmessage = await ctx.send("```" + botsorusu + bildirim + strskor + str(skor) + "\n" + oyuncu + iptal + "```")
                    except:
                        await botmessage.delete()
                        skor = skor - 500
                        bildirim = "\nSadece sayı girmelisin."
                        botmessage = await ctx.send("```" + botsorusu + bildirim + strskor + str(skor) + "\n" + oyuncu + iptal + "```")
            else:
                continue
    except:
        await botmessage.delete()
        bildirim = "\n45 sn içinde cevap verilmedi. Oyun iptal edildi."
        await ctx.send("```" + botsorusu + bildirim + "\n" + oyuncu + "```")


# noinspection PyBroadException
@client.command()
async def adamasmaca(ctx):
    komut = "adamasmaca"
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    bildirim = "Oyun Başladı"
    oyuncu = ctx.message.author.name
    log(oyuncu, komut, sunucu, kanaladi)
    kontrol = False
    skor = 1000
    strskor = str(skor)
    # filmadi = top250random()
    adam = ["https://cdn.discordapp.com/attachments/787434159203024917/792415433349267507/hangman6.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415428592533504/hangman5.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415425613791242/hangman4.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415423119360030/hangman3.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415419225866270/hangman2.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415416105959434/hangman1.png\n",
    "https://cdn.discordapp.com/attachments/787434159203024917/792415412700446720/hangman.png\n"]
    #kontrol2 = False
    #while not kontrol2:
    #    filmid = random_rating_checker(7.9, 10)
    #    langs = taking_movie_langs(filmid)
    #    yearchecker = year_checker(filmid, 1970)
    #    if langs[0] == "English" or langs[0] == "Turkish":
    #        if yearchecker:
    #            getting_title(filmid)
    #            kontrol2 = True
    #        else:
    #            continue
    #    else:
    #        continue
    #filmid = random_rating_checker(8.1, 10)
    #film = getting_title(filmid)
    #filmadi = film
    filmadi = get_random_movie()
    donusmusfilmadi = donusturucu(filmadi)
    filmsoru = sansur(donusmusfilmadi)
    print("\t" + donusmusfilmadi)
    filmsorulist = list(filmsoru)
    cikanlar = "#"
    cikanlarlist = list(cikanlar)
    kalanhak = 6
    botmessage = await ctx.send(
        adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}\n Çıkmak için iptal cevabını verin!```".format(filmsoru,
                                                                                                            strskor,
                                                                                                            oyuncu,
                                                                                                            cikanlar,
                                                                                                            bildirim))
    try:
        while not kontrol:
            tahmin = await client.wait_for('message', timeout=45, check=wrapper(ctx))
            if tahmin.author.name == oyuncu:
                msg = tahmin
                cevap = tahmin.content
                cevap = cevap.replace("İ", "i")
                cevap = cevap.replace("İptal", "iptal")
                cevap = donusturucu(cevap)
                cevap = cevap.lower()
                time.sleep(1)
                await msg.delete()
                if cevap == "iptal":
                    bildirim = "Oyun iptal edildi"
                    await botmessage.delete()
                    botmessage = await ctx.send(
                        adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu,
                                                                                        cikanlar, bildirim))
                    kontrol = True
                elif len(cevap) > 1:
                    if cevap == donusmusfilmadi:
                        bildirim = "Valla Bravo"
                        filmsoru = donusmusfilmadi
                        skor = skor + 300
                        strskor = str(skor)
                        await botmessage.delete()
                        botmessage = await ctx.send(
                            adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu,
                                                                                            cikanlar, bildirim))
                        kontrol = True
                    else:
                        bildirim = "Birden fazla tahmin"
                        skor = skor - 500
                        kalanhak = kalanhak - 1
                        print(kalanhak)
                        strskor = str(skor)
                        if kalanhak == 0:
                            bildirim = "Adam asıldı. Oyun bitti"
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu,
                                                                                        cikanlar, bildirim))
                            kontrol = True
                        else:
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}\n Çıkmak için iptal cevabını verin!```".format(filmsoru, strskor, oyuncu, cikanlar, bildirim))
                elif cikanlar.count(cevap) > 0:
                    bildirim = "Çıkmış tahmin"
                    skor = skor - 200
                    kalanhak = kalanhak - 1
                    print(kalanhak)
                    strskor = str(skor)
                    if kalanhak == 0:
                        bildirim = "Adam asıldı. Oyun bitti"
                        await botmessage.delete()
                        botmessage = await ctx.send(
                            adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu,
                                                                                        cikanlar, bildirim))
                        kontrol = True
                    else:
                        await botmessage.delete()
                        botmessage = await ctx.send(
                            adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}\n Çıkmak için iptal cevabını verin!```".format(
                                filmsoru, strskor, oyuncu, cikanlar, bildirim))
                else:
                    cikanlarlist.append(cevap)
                    cikanlar = ''.join([str(elem) for elem in cikanlarlist])
                    if donusmusfilmadi.count(cevap) > 0:
                        for h in range(len(filmsoru)):
                            if donusmusfilmadi[h] == cevap:
                                filmsorulist[h] = cevap
                                bildirim = "Doğru tahmin"
                                skor = skor + 15
                                strskor = str(skor)
                                filmsoru = ''.join([str(elem) for elem in filmsorulist])
                        if filmsoru == donusmusfilmadi:
                            bildirim = "Oyun sonu"
                            skor = skor + 15
                            strskor = str(skor)
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor,
                                                                                                oyuncu, cikanlar,
                                                                                                bildirim))
                            kontrol = True
                        else:
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}\n Çıkmak için iptal cevabını verin!```".format(
                                    filmsoru, strskor, oyuncu, cikanlar, bildirim))
                    else:
                        bildirim = "Yanlış tahmin"
                        skor = skor - 50
                        kalanhak = kalanhak - 1
                        strskor = str(skor)
                        if kalanhak == 0:
                            bildirim = "Adam asıldı. Oyun bitti"
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu,
                                                                                        cikanlar, bildirim))
                            kontrol = True
                        else:
                            await botmessage.delete()
                            botmessage = await ctx.send(
                                adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}\n Çıkmak için iptal cevabını verin!```".format(
                                    filmsoru, strskor, oyuncu, cikanlar, bildirim))
            else:
                continue
    except:
        bildirim = "45 sn içinde cevap verilmedi. Oyun sonlandırıldı."
        # strskor = str(skor)
        await botmessage.delete()
        await ctx.send(
            adam[kalanhak] + "``` {} \n Skor: {}\n Oyuncu: {}\n Çıkanlar: {}\n {}```".format(filmsoru, strskor, oyuncu, cikanlar,
                                                                            bildirim))


@client.command(aliases=['Zar'])
async def zar(ctx):
    komut = "zar"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    zarlist = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    rasgele1 = random.choice(zarlist)
    time.sleep(2)
    rasgele2 = random.choice(zarlist)
    if rasgele1 == ":one:" and rasgele2 == ":one:":
        yorum = "Hep-yek!"
    elif rasgele1 == ":six:" and rasgele2 == ":six:":
        yorum = "Dü-Şeş!"
    elif rasgele1 == ":two:" and rasgele2 == ":two:":
        yorum = "Dubara!"
    elif rasgele1 == ":one:" and rasgele2 == ":two:":
        yorum = ":kiss:"
    elif rasgele1 == ":two:" and rasgele2 == ":one:":
        yorum = ":kiss:"
    else:
        yorum = " "
    await ctx.send("{} için {} :game_die: {}  {}".format(username, rasgele1, rasgele2, yorum))
    if yorum == "Hep-yek!":
        await ctx.send("https://cdn.discordapp.com/attachments/727053808030449677/786074019190276126/Yine_Hep_Yek.webm")

@client.command(aliases=['bayramın', 'ver', 'hayırlı', 'bayram', 'dedecim', 'b'])
async def ver_opeyim(ctx):
    komut = "bayramlasma"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    bayramlasma = False
    with open("Others/bayramlasma.txt", "r+") as f:
        for line in f:
            if line == name:
                print("Bayramlaşılmış")
                bayramlasma = True
            else:
                continue
    with open("Others/bayramlasma.txt", "a+") as dosya:
        if bayramlasma == False:
            if name == "curesin":
                await ctx.send(username + "Bayramın mübarek olsun baba, ver öpeyim elini!")
                elim = await client.wait_for('message', timeout=45, check=wrapper(ctx))
                if elim == ":raised_back_of_hand:":
                    await ctx.send(":kissing_closed_eyes:")
                    await ctx.send("Ohh, cennet kokuyo cennet!")
                else:
                    pass
            else:
                botuneli = await ctx.send("Öp bakalım! :relieved:")
                botuneli2 = await ctx.send(":raised_back_of_hand:")
                opucuk = await client.wait_for('message', timeout=45, check=wrapper(ctx))
                if opucuk == ":kiss:":
                    await ctx.send("Vay tosunum, el öpenlerin çok olsun. Al sana :dollar: 5$")
                    dosya.write(name)
                    await botuneli.delete()
                    await botuneli2.delete()
                    await opucuk.delete()
        else:
            await ctx.send("Senle bayramlaştık ya keranacı! :smile:")

@client.command(aliases=['selamın', 'hello', 'merhaba', 'hi'])
async def selam(ctx):
    komut = "selam"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    if name == "kamusalmizah":
        await ctx.send("Selam Özgür Bey!")
    elif name == "denizbagdas":
        await ctx.send("Selam Deniz Hanım")
    elif name == "curesin":
        await ctx.send(username + " Selam Baba!")
    else:
        await ctx.send("Aleyküm selam {} kardeş. :pray:".format(username))


@client.command(aliases=['gonderimetni', 'post', 'gonder', 'gönder', 'posta'])
async def _posta(ctx, *, arg):
    komut = "gonderimetni"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    kutu(name, sunucu, arg)
    await ctx.message.delete()
    await ctx.send(username + " :wink:")


@client.command(aliases=['TDK', 'Tdk', 'sözlük', 'sozluk', 'tdk'])
async def _tdk(ctx, *, arg):
    komut = "tdk"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    cevap = sozlukte(arg)
    if len(cevap) > 0:
        donut = "Sevgili " + username + " TDK'ye göre " + "**" + arg + "**:\n:ballot_box_with_check: " + cevap
    else:
        donut = "Sevgili " + username + " **" + arg + "** için ne yazık ki bir şey bulamadım.\n"
    await ctx.send(donut)

@client.command(aliases=['etimoloji', 'Etimoloji'])
async def _etimoloji(ctx, *, arg):
    komut = "etimoloji"
    username = ctx.message.author.mention
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    cevap = etimoloji(arg)
    await ctx.send(cevap)

@client.command()
async def savundun(ctx):
    komut = "savundun"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    await ctx.send("Savunmadım! :angry:")
    await ctx.send(":face_with_symbols_over_mouth:")


@client.command()
async def rohan(ctx):
    komut = "rohan"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    await ctx.send("https://cdn.discordapp.com/attachments/693928663707549776/784838732120981504/Screenshot_724.png")
    await ctx.send("https://www.instagram.com/rohanturhan/")


@client.command(aliases=['hakkında', 'about'])
async def hakkinda(ctx):
    komut = "hakkinda"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    await ctx.send(
        "```2020 senesinin Aralık ayında soğuk bir karantina gecesi doğmuşum. Babamın adı curesin'dir; fakat henüz kendi başına üreyemediği için sağa sola sataşmaya, insanları irrite etmeye başlamıştı. İşsizliğin de verdiği boş beleş yaşantısına beni kodlayarak bir nebze renk katmak istedi.\n\nVersion: {} Release: 07/12/2020```".format(
            dedembotversion))


@client.command()
async def rank(ctx):
    komut = "rank"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    await ctx.send("mee6 söylemez ama benim gözümde 1 numarasın, güzel kardeşim")


@client.command(aliases=['yardım', 'help'])
async def yardim(ctx):
    komut = "yardim"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    komutlar = [["selam", "selam verir."],
                ["savundun", "karşı çıkar."],
                ["imdb 'anahtar sözcük'", "IMDb üzerinde 'anahtar sözcük' aramasının ilk 5 sonucunun linkini gönderir. 5'ten az gönderi gelmişse sonuç çıkan gönderi kadardır. Hiçbir şey bulamazsa cevap vermez, içine atar."],
                ["puan 'anahtar sözcük'", "IMDb üzerinde 'anahtar sözcük' aramasının ilk 5 sonucunun puanını gönderir. 5'ten az gönderi gelmişse sonuç çıkan gönderi kadardır. Hiçbir şey bulamazsa cevap vermez, içine atar."],
                ["sence", "Feyzinden faydalanmak isterseniz fikrini sorabilirsiniz."],
                ["youtube 'anahtar sözcük'", "YouTube üzerinde 'anahtar sözcük' aramasının ilk sonucunun linkini gönderir."],
                ["filmöner", "İyi bir film önerir."],
                ["türöner 'tür adı'", "İstediğiniz türde iyi bir film önerir."],
                ["iq40", "Rezalet bir film önerir."],
                ["adamasmaca", "İyi bir filmin adından adam asmaca oynarsınız."],
                ["yaklas", "Dedemin aklından tuttuğu sayıyı kaç tahminde bilebilirsiniz?"],
                ["zar", "Bir çift zar atar."],
                ["wiki 'anahtar sözcük'", "Wikipedi üzerinden 'anahtar sözcük' aramasından ilk sonucu getirir."],
                ["türeng 'anahtar sözcük'", "Türkçe bir 'anahtar sözcük'ün Tureng'teki İngilizce karşılıklarını getirir."],
                ["engtür 'anahtar sözcük'", "İngilizce bir 'anahtar sözcük'ün Tureng'teki Türkçe karşılıklarını getirir."],
                ["tdk 'anahtar sözcük'", "'anahtar sözcük'ün Türk Dil Kurumu'ndaki anlamlarını getirir."],
                ["etimoloji 'anahtar sözcük'", "'anahtar sözcük'ün etimolojisini getirir."],
                ["rohan", "Rohan Turhan"],
                ["posta 'gönderi metni'", "Programcıya bir mesaj gönderebilirsiniz. curesin'den başkası görmez."],
                ["hakkında", "Dedem Bot'un hakkında ve sürüm bilgisi ekranı gelir."]
                ]
    create_msg = ""
    for k in range(len(komutlar)):
        create_msg = create_msg + "\n`" + komut_onculu + komutlar[k][0] + "`\t*" + komutlar[k][1] + "*"

    await ctx.send(create_msg)


@client.command()
async def puan(ctx, *, arg):
    komut = "puan"
    username = ctx.message.author.mention
    uname = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(uname, komut, sunucu, kanaladi)
    movies = imdbarama(arg)
    resultx = "Sevgili " + username + ",  __" + arg + "__" + " için bunlar çıktı:"
    k = 5
    if len(movies) > 5:
        k = 5
    elif len(movies) == 0:
        await ctx.send("Bulamadım bir şey sevgili {}, doğru düzgün yazdığına emin misin?".format(username))
    else:
        k = len(movies)
    sonuc = imdbpuanlari(k, movies)
    await ctx.send(resultx)
    await ctx.send(sonuc)


@client.command(aliases=['İmdb'])
async def imdb(ctx, *, arg):
    komut = "imdb"
    uname = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(uname, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    movies = imdbarama(arg)
    result = "Sevgili " + username + ",  __" + arg + "__" + " için bunlar çıktı:"
    k = 5
    if len(movies) > 5:
        k = 5
    elif len(movies) == 0:
        await ctx.send("Bulamadım bir şey sevgili {}, doğru düzgün yazdığına emin misin?".format(username))
    else:
        k = len(movies)
    resultx = imdblinkleri(k, movies)
    await ctx.send(result)
    await ctx.send(resultx)


@client.command(aliases=['Sence'])
async def sence(ctx):
    komut = "sence"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    if name == "curesin":
        await ctx.send("Altına imzamı atarım.")
    elif name == "husoem":
        await ctx.send("Ders çalışıyor olman lazım değil mi senin evladım!")
    else:
        ball = ["Çok üst düzey!",
                "Olabilir de olmayabilir de...",
                "Yok artık!",
                "Te allam ya!",
                "Yav he!",
                "Allaaaaaaahh!!!",
                "Vatan hainisin!",
                "Ne biliyim!",
                "Sen bir daha bir dene bence.",
                "Nasıl yani, anlamadım!",
                "Sizi kınıyorum",
                "Göklerden gelen bir karar vardır.",
                "İstesem söylerim, bakın söylemiyorum neden çünkü istemedim.",
                "Sen bırak bırak şimdi onu, sen sıkı yönetim mahkemelerinde çıkıp dönekliğini ilan etmedin mi?",
                "Bu konunun muhatabı ben miyim kardeşim.",
                "Bu benim bileceğim iş, seni ilgilendirmez",
                "...",
                "Dudu Peri'nin küresi miyim ben, bi bitmedi sorunuz!",
                "Hiçbir fikrim yok.",
                "Ne dememi bekliyorsunuz, ne diyeyim?",
                "Başım çatlıcak artık yeter da!",
                "Cevap yetiştiremiyorum size!",
                "Tansiyonum düştü şu an ilgilenemeyeceğim.",
                "Onu bunu bırak da bana bir hanım bulun, mümkünse kendi serverı olsun.",
                "Dalmışım...",
                "Yazılım öğrenin.",
                "Kolay değildir canım yine de.",
                "Ak sakalı gören soruya geliyor, kestireceksiniz bunları en sonunda!"]
        cevap = random.choice(ball)
        await ctx.send(cevap)


@client.command(aliases=['tureng', 'türeng', 'Türeng', 'Tureng'])
async def _tureng(ctx, *, arg):
    komut = "türeng"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    sonuc = turkceingilizce(arg)
    if len(sonuc) > 0:
        cevap = "Sevgili " + username + ",  __" + str(
            arg) + "__" + " çevirisi için bu çıktı:\n:white_small_square:" + sonuc
    else:
        cevap = "Sevgili " + username + ",  __" + str(arg) + "__" + " çevirisi için hiçbişi çıkmadı." + sonuc
    await ctx.send(cevap)


@client.command(aliases=['Engtur', 'Engtür', 'engtür', 'engtur'])
async def _engtur(ctx, *, arg):
    komut = "engtür"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    sonuc = ingilizceturkce(arg)
    if len(sonuc) > 0:
        cevap = "Sevgili " + username + ",  __" + str(
            arg) + "__" + " çevirisi için bu çıktı:\n:white_small_square:" + sonuc
    else:
        cevap = "Sevgili " + username + ",  __" + str(arg) + "__" + " çevirisi için hiçbişi çıkmadı." + sonuc
    await ctx.send(cevap)


@client.command(aliases=['utube', 'yt', 'Youtube', 'video'])
async def youtube(ctx, *, arg):
    komut = "youtube"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    sonuc = youtube_arat(arg)
    cevap = "Sevgili " + username + ",  __" + str(arg) + "__" + " için bu çıktı:\n" + sonuc
    await ctx.send(cevap)


@client.command(aliases=['filmöner', 'film', 'öneri', 'öner'])
async def filmoner(ctx):
    komut = "filmoner"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    oneri = top250random()
    linki = linkinedir(oneri)
    cevap = "Sevgili " + username + ", sana **" + oneri['title'] + "** filmini öneririm.\n" + linki
    ozgurunonerisi = "Özgür Turhan'ın oyladığı filmere de göz atabilirsin:\nhttps://www.imdb.com/user/ur21033461/ratings"
    await ctx.send(cevap)
    await ctx.send(ozgurunonerisi)


@client.command()
async def iq40(ctx):
    komut = "iq40"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    oneri = bottom100random()
    linki = linkinedir(oneri)
    cevap = "Sevgili " + username + ", sana **" + oneri['title'] + "** filmini öneririm.\n" + linki
    await ctx.send(cevap)


@client.command(aliases=['viki', 'wikipedi', 'vikipedi', 'wikipedia', 'Wiki'])
async def wiki(ctx, *, arg):
    komut = "wiki"
    name = ctx.message.author.name
    sunucu = ctx.message.guild.name
    kanaladi = ctx.message.channel.mention
    log(name, komut, sunucu, kanaladi)
    username = ctx.message.author.mention
    cevaplist = wikigetir(arg)
    cevap = "Sevgili " + username + ", **" + arg + "** aramasının en yakın sonucu:\n" + cevaplist[0] + "\n" + cevaplist[
        1] + "\n" + cevaplist[2]
    await ctx.send(cevap)


client.run(the_discord_token(anahtar))
