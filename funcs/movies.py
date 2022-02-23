from webbrowser import get
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API_KEY')


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    #return trending_movies[:5]
    x = trending_movies[:5]
    y = ', '.join(x)
    return y

#to_print = get_trending_movies()
#print(to_print) for testing