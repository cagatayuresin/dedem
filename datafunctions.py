import pandas as pd
import random

moviesdata = pd.read_csv("movies/IMDb movies.csv")

original_title = moviesdata["original_title"]
global_title = moviesdata["title"]
imdb_rating = moviesdata["avg_vote"]
movie_lang = moviesdata["language"]
movie_country = moviesdata["country"]
movie_genres = moviesdata["genre"]
movie_director = moviesdata["director"]
movie_writer = moviesdata["writer"]
movie_actors = moviesdata["actors"]
movie_imdb_tt_id = moviesdata["imdb_title_id"]
movie_production = moviesdata["production_company"]
movie_description = moviesdata["description"]
movie_year = moviesdata["year"]


def random_rating_checker(down, up):
    kontrol = False
    up = float(up)
    down = float(down)
    while not kontrol:
        i = random.randint(0, 85850)
        print(i)
        if imdb_rating[i] is None:
            continue
        else:
            rating = str(imdb_rating[i])
            print(rating)
            if rating != "None":
                rating = rating.replace(",", ".")
                rating = float(rating)
                if down < rating < up:
                    print(rating)
                    return i
                else:
                    continue
            else:
                continue


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


"""        if movie_adult[i] == 'False':
            print(movie_adult[i])
            if movie_lang[i] == 'en' or movie_lang[i] == 'tr':
                print(movie_lang[i])
                a = str(imdb_rating[i])
                b = a.replace(",",".")
                c = float(b)
                print(type(c))
                print(c)
                if c >= down and c <= up:
                    return global_title[i]
                    kontrol = True
                else:
                    continue
            else:
                continue
        else:
            continue
"""

"""def random_movie(down, up):
    kontrol = False
    while kontrol == False:
        i = random.randint(0,45465)
        print(i)
        try:
            if movie_adult[i] == 'False':
                print(movie_adult[i])
                if movie_lang[i] == 'en' or movie_lang[i] == 'tr':
                    print(movie_lang[i])
                    v = float(imdb_rating[i].replace(',','.'))
                    type(v)
                    if v >= down and v <= up:
                        print(v)
                        the_link = "https://www.imdb.com/title/"+movie_imdb_tt_id[i]
                        print(the_link)
                        if movie_genres[i] != "[]" and movie_production[i] != "[]":
                            print(movie_genres[i])
                            print(type(movie_genres[i]))
                            print(movie_production[i])
                            print(type(movie_production[i]))
                            print(movie_production[i])
                            genresstr = movie_genres[i]
                            genresstr = genresstr.translate({ord(z): None for z in "[]"})
                            listgenres1 = list(genresstr.split(", "))
                            print(listgenres1)
                            productionsstr = productionssstr.translate({ord(z): None for z in "[]"})
                            listproductions1 = list(productionsstr.split(", "))
                            print(listproductions1)
                            genres = []
                            for p in range(len(listgenres1)):
                                listgenres2 = ast.literal_eval(listgenres1[p])
                                genre = listgenres2['name']
                                print(genre)
                                genres.append(genre)
                            print(genres)
                            productions = []
                            for p in range(len(listproductions1)):
                                listproductions2 = ast.literal_eval(listproductions1[p])
                                production = listproductions2['name']
                                print(production)
                                productions.append(production)
                            print(productions)
                            try:
                                #the_list = [original_title[i], global_title[i], movie_release_date[i], imdb_rating[i], genres, productions, movie_overview[i], movie_lang, the_link]
                                the_list = global_title[i]
                                print(the_list)
                                break
                                return the_list

                            except:
                                kontrol = True
                                print("Except2")
                                #continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

            else:
                continue
        except:
            kontrol = True
            print("Except1")
            #continue
        return the_list

"""
