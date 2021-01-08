import pandas as pd
import random

moviesdata = pd.read_csv("movies/movies.csv", encoding="ISO-8859-1", delimiter=';')

original_title = moviesdata["original_title"]
imdb_rating = moviesdata["avg_vote"]


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


def getting_title(i):
    title = str(original_title[i])
    return title
