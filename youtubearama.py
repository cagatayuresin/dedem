from youtubepy import Video

def youtube_arat(s):
    Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
    arama = s.lower()
    arama = arama.translate(Tr2Eng)
    video = Video(arama)
    sonuc = video.search()
    return sonuc
