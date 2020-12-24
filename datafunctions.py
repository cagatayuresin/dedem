import pandas as pd
import random

moviesdata = pd.read_csv("movies/movies.csv", encoding = "ISO-8859-1", delimiter= ';')

original_title = moviesdata["original_title"]
#global_title = moviesdata["title"]
imdb_rating = moviesdata["avg_vote"]
#movie_lang = moviesdata["language"]
#movie_country = moviesdata["country"]
#movie_genres = moviesdata["genre"]
#movie_director = moviesdata["director"]
#movie_writer = moviesdata["writer"]
#movie_actors = moviesdata["actors"]
#movie_imdb_tt_id = moviesdata["imdb_title_id"]
#movie_production = moviesdata["production_company"]
#movie_description = moviesdata["description"]
#movie_year = moviesdata["year"]

def random_rating_checker(down, up):
    kontrol = False
    up = float(up)
    down = float(down)
    counter = 0
    while not kontrol:
        i = random.randint(0, 85850)
        counter += 1
        if imdb_rating[i] is None:
            continue
        else:
            rating = str(imdb_rating[i])
            if rating != "None":
                rating = rating.replace(",", ".")
                rating = float(rating)
                if down < rating < up:
                    print(str(i) + "\t" + str(rating) + "\t" + str(counter) + " film tarandı.")
                    return i
                else:
                    continue
            else:
                continue

def get_random_movie():
    i = random.randint(0, 2019)
    title = getting_title(i)
    return title

def taking_movie_langs(i):
    if movie_lang[i] is None:
        return ["None"]
    else:
        langs = movie_lang[i]
        langs = str(langs)
        print(langs)
        if langs != "None":
            langs = langs.split(", ")
            return langs
        else:
            return ["None"]

def getting_title(i):
    title = str(original_title[i])
    return title

def getting_year(i):
    if movie_year[i] is not None:
        year = movie_year[i]
        year = str(year)
        return year
    else:
        year = "0"
        return year

def year_checker(i, down):
    year = getting_year(i)
    year = int(year)
    if year >= down:
        return True
    else:
        return False