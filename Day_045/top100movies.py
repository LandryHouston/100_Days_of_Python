import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = [movie.text.strip() for movie in soup.find_all("h2") if ")" in movie.text[:4]][::-1] # Reverse the order of the list

with open("movies.txt", "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(movie + "\n")