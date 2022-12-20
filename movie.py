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
    def __init__(self, title, year, kind, genre):
        self.title = title
        self.year = year
        self.kind = kind
        self.genre = genre

        self._play = 0

    @property
    def play(self):
        return self._play

    @property
    def info(self):
        return f'"{self.title} ({self.year})'
    @property
    def type(self):
        print(type(self).__name__)

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
    @property
    def type(self):
        print(type(self).__name__)
    @property
    def play(self):
        return self._play
    @play.setter
    def play(self, value):
        self._play += 1

movie_db = []


def append_title(db_title):
    return movie_db.append(db_title)


def create_movie_database(insert):
    for q in range(insert):
        a = random.randrange(len_title_db)
        input_title = title_db[a]
        input_year = random.randrange(1945, 2022)
        b = random.randrange(len_genre_db)
        input_genre = genre_db[b]
        input_series = random.randint(1, 2)
        if input_series == 2:
            input_kind = 'Serie'
            input_seasons = random.randint(1, 15)
            input_episodes = random.randint(5, 25)
            for m in range(input_seasons):
                for n in range(input_episodes):
                    db_title = Series(title=input_title, year=input_year, kind=input_kind, genre=input_genre, episode="{0:02d}".format(input_episodes),
                                      season="{0:02d}".format(input_seasons))
                    movie_db.append(db_title)
        else:
            input_kind='Movie'
            db_title = Movie(title=input_title, year=input_year, kind=input_kind, genre=input_genre)
            movie_db.append(db_title)


insert = int(input("Podaj ilość tytułów: "))
print('Biblioteka filmów')
create_movie_database(insert)


def get_movies():
    db_list = []
    for i in range(len(movie_db)):
        if movie_db[i].__class__.__name__ == 'Movie':
            movie_title = movie_db[i].title
            db_list.append(movie_title)
    sorted_db_list = sorted(db_list)


def get_series():
    db_list = []
    for i in range(len(movie_db)):
        if movie_db[i].__class__.__name__ == 'Series':
            db_list.append(movie_db[i].title)
    sorted_db_list = sorted(db_list)


def search():
    searching_title = input('Podaj tytuł: ')
    for i in range(len(movie_db)):
         if movie_db[i].title == searching_title:
            print(f'Znaleziono {movie_db[i].title}')


def generate_views():
    i = random.randrange(len(movie_db))
    movie_db[i]._play += random.randrange(100)


def generate_views_10():
    plays = []
    titles = []
    views_dict = {}
    sorted_views_dict = {}
    i = random.randrange(len(movie_db))
    for j in range(10):
        i = random.randrange(len(movie_db))
        movie_db[i]._play += random.randrange(100)
        plays.append(movie_db[i]._play)
        titles.append(movie_db[i].info)
    for q in range(len(plays)):
        views_dict[plays[q]] = titles[q]
    sorted_views_dict = sorted(views_dict.items(), reverse=True)
    i = 0
    for j in sorted_views_dict:
        if i == 3:
            break
        print(sorted_views_dict[i])
        i +=1

print(f'Najpopularniejsze filmy i seriale dnia {date.today()} to:')
generate_views_10()