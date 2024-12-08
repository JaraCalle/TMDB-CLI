from decouple import config
import requests

class Tmdb():
    def __init__(self):
        self.url = "https://api.themoviedb.org"
        self.headers = {
            "accept": "application/json",
            "Authorization": config("TMDB_API_KEY")
        }
    
    def get_movies(self) -> dict:
        url = f"{self.url}/3/trending/movie/day?language=es-MX"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_popular_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/popular?language=es-MX&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_now_playing_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/now_playing?language=es-MX&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_top_rated_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/top_rated?language=es-MX&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_upcoming_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/upcoming?language=es-MX&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()