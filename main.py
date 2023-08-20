import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
def custom_sort(elem):
    return int(elem.split(')')[0])

response = requests.get(URL)
empire_webpage = response.text

movies_list =[]

soup = BeautifulSoup(empire_webpage , "html.parser")

movies = soup.find_all(name = "h3", class_ = "listicleItem_listicle-item__title__hW_Kn")

for movie in movies :
    movie_name = movie.getText()
    movies_list.append(movie_name)

sorted_list = sorted(movies_list, key=custom_sort)

with open("movies.txt", 'w') as file:
        for item in sorted_list:
            file.write("%s\n" % item)