favorite_movies = [
    {"name": "The Matrix I", "release_year": 1999},
    {"name": "Star Wars IV", "release_year": 1977},
    {"name": "Spirited Away", "release_year": 2001},
    {"name": "The Lord of the Rings: The Fellowship of the Ring", "release_year": 2001},
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)