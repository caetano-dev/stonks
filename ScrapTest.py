import requests
from bs4 import BeautifulSoup
from random import randint

headers = {"UserAgent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
URL = 'https://www.youtube.com/results?search_query=stonks'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
videos = []

for link in soup.find_all('a'):
    links = (link.get('href'))
    if "/watch?v=" in links and "https" not in links and "radio=" not in links:  #20 links
        videos.append(links)

x = randint(0,19)
print(videos[x])
