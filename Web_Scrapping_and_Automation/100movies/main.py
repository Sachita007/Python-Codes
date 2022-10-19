from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
movies_list = [movies.getText() for movies in soup.find_all(name="h3", class_="title")]
movies_list.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movies in movies_list:
        file.write(movies + "\n")
