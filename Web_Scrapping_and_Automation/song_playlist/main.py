from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

USERID = "556c49eb9ef5490bb2a4aa5a05ea1168"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

song_site = response.text

soup = BeautifulSoup(song_site, "html.parser")
song_tite = soup.find_all(name="h3", class_="a-no-trucate")

song_list = []
for song in song_tite:
    song_list.append(song.getText().strip())

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=USERID,
                                               client_secret="c77ac7c7bebc4718b140ff4c44089d84",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog = True,
                                               cache_path = "token.txt",))
user_id =  sp.current_user()["id"]

song_uries = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uries.append(uri)
    except IndexError:
        print(f"{song} is doesn't exist in spotify. Skipped")
# print(song_uries)


playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uries)


# song = sp.search(q=f"track:{song_list[0]} year:{2001}", type="track")
# result = song["tracks"]["items"][0]["uri"]
# print(song)
# pprint(result)


