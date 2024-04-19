class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy (Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print (f'Комедии: {self.movies}')

class Drama (Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print (f'Драмы: {self.movies}')

m1=Comedy()
m1.add_movie('Большой куш')

m2=Drama()
m2.add_movie('Оружейный барон')