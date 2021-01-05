import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

headlines = []

url = "https://www.marketwatch.com/latest-news?mod=top_nav"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

headline_div = soup.find_all('div', class_='element element--article')


for container in headline_div:
    name = container.div.h3.find('a', class_='link')
    headlines.append(name)


titles = pd.DataFrame ({
    "Headlines" : headlines,
})

print(titles)
