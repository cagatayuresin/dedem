import imdb
import random
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
