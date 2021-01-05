import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 

headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

titles = []
years = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:

    name = container.h3.a.text
    titles.append(name)

    year = container.h3.find('span', class_ ='lister-item-year').text
    years.append(year)

movies = pd.DataFrame({
    'movie': titles,
    'year' : years,
})



movies.to_csv('movies.csv')
print(movies)