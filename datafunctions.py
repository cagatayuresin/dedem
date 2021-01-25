import pandas as pd
import random

moviesdata = pd.read_csv("movies/movies.csv", encoding="ISO-8859-1", delimiter=';')

original_title = moviesdata["original_title"]
imdb_rating = moviesdata["avg_vote"]
genres = moviesdata["genre"]
imdbid = moviesdata["imdb_title_id"]
year = moviesdata["year"]


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


def get_random_movie():
    i = random.randint(0, 2019)
    title = getting_title(i)
    return title


def getting_title(i):
    title = str(original_title[i])
    return title
