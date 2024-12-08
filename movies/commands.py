import typer
from utils.API import Tmdb
from .models import json_to_movies

tmdb = Tmdb()
movies_app = typer.Typer()

@movies_app.command()
def movies(type: str = typer.Option(None, help="Tipo de pelicula según TMDB")):
    if type == "popular":
        movies = json_to_movies(tmdb.get_popular_movies())

    if type == "playing":
        movies = json_to_movies(tmdb.get_now_playing_movies())

    if type == "top":
        movies = json_to_movies(tmdb.get_top_rated_movies())
    
    if type == "upcoming":
        movies = json_to_movies(tmdb.get_upcoming_movies())

    if not type:
        movies = json_to_movies(tmdb.get_movies())

    for movie in movies:
        print(f"-> {movie}")