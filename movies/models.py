class Movie():
    def __init__(self):
        self.title = ""
        self.release_date = ""
    
    def set_title(self, title):
        self.title = title
        return self
    
    def set_release_date(self, release_date):
        self.release_date = release_date
        return self
    
    def __str__(self):
        return f"{self.title} [{self.release_date}]"

def json_to_movies(json):
    movies = []
    for movie in json["results"]:
        m = Movie().set_title(movie["title"]).set_release_date(movie["release_date"])
        movies.append(m)
    return movies