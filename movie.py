from imdb import Cinemagoer
from datetime import date
import random
ia = Cinemagoer()
title_db = []
genre_db = []

for j in range(10):
    i = str(random.randint(1, 500))
    movie = ia.get_movie(i)
    title_db.append(movie)
    for genre in movie['genres']:
        genre_db.append(genre)
len_title_db = len(title_db)
len_genre_db = len(genre_db)


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        # self.kind = kind
        self.genre = genre

        self._play = 0

    @property
    def play(self):
        return self._play

    @property
    def info(self):
        return f'"{self.title} ({self.year})'
    # @property
    # def type(self):
    #     print(type(self).__name__)

    @play.setter
    def play(self, value):
        self._play += 1


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    @property
    def info(self):
        s =  f'{self.season:2}'
        e = f'{self.episode:2}'
        return f"{self.title} S {s} E {e}"


movie_db = []


def create_movie_database(quantity):
    database = []
    for i in range(1, quantity+1):
        cinemagoer_entity = ia.get_movie(i)
        if cinemagoer_entity["kind"] == "movie":
            movie = Movie(
                title=cinemagoer_entity["title"],
                year=cinemagoer_entity["year"],
                genre=cinemagoer_entity["genre"][0],
            )
        else:
            movie = Series(
                title=cinemagoer_entity["title"],
                year=cinemagoer_entity["year"],
                genre=cinemagoer_entity["genre"][0],
                episode="{0:02d}".format(random.randint(1, 25)),
                season= "{0:02d}".format(random.randint (1, 5)),
            )
        database.append(movie)


def get_movies():
    db_list = []
    for movie in movie_db:
        if movie.__name__ == 'Movie':
            db_list.append(movie.title)
    sorted_db_list = sorted(db_list)


def get_series():
    db_list = []
    for movie in movie_db:
        if movie_db[i].__class__.__name__ == 'Series':
            db_list.append(movie.title)
    sorted_db_list = sorted(db_list)


def search():
    searching_title = input('Podaj tytuł: ')
    for movie in movie_db:
         if movie_db[i].title == searching_title:
            return f'Znaleziono {movie_db[i].title}'


def generate_views(n=10):
    views_dict ={}
    sorted_views_dict ={}
    movies = random.choices(movie_database, k=n)
    for movie in movies:
        movie.play += random.randint(1, 10)
        views_dict[movie.play] = movie.title
    sorted_views_dict = sorted(views_dict.items() ,  reverse= True)
    for i in sorted_views_dict:
        if i == 3:
            break
        print(sorted_views_dict[i])


# def generate_views_10():
#     plays = []
#     titles = []
#     views_dict = {}
#     sorted_views_dict = {}
#     movies = random.choices(movie_database, k=n)
#     for j in range(10):
#         i = random.randrange(len(movie_db))
#         movie_db[i]._play += random.randrange(100)
#         plays.append(movie_db[i]._play)
#         titles.append(movie_db[i].info)
#     for q in range(len(plays)):
#         views_dict[plays[q]] = titles[q]
#     sorted_views_dict = sorted(views_dict.items(), reverse=True)
#     i = 0
#     for j in sorted_views_dict:
#         if i == 3:
#             break
#         print(sorted_views_dict[i])
#         i +=1


movie_database = create_movie_database(100)
print('Biblioteka filmów')
print(f'Najpopularniejsze filmy i seriale dnia {date.today()} to:')
generate_views()