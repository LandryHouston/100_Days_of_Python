import yaml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=config['SPOTIFY_CLIENT_ID'],
        client_secret=config['SPOTIFY_CLIENT_SECRET'],
        show_dialog=True,
        cache_path="token.txt",
        username=config['SPOTIFY_USERNAME'], 
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(song)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)