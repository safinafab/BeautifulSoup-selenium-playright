URL ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
from bs4 import BeautifulSoup
import requests

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content,"html.parser")
# scrape=soup.prettify()

all_movies = soup.find_all(name="h3",class_="title")
# print(all_movies)

movies =[i.getText() for i in all_movies]
#to reverse the list
sorted_movies = movies[::-1]

with open("movie_data.txt",mode="w", encoding="utf-8") as file:
    for movie in sorted_movies:
        file.write(f"{movie}""\n")
        
