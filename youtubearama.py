from youtubepy import Video

def youtube_arat(s):
    tr2_eng = str.maketrans("çğıöşü", "cgiosu")
    arama = s.lower()
    arama = arama.translate(tr2_eng)
    video = Video(arama)
    sonuc = video.search()
    return sonuc
