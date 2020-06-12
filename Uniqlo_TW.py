import requests
from bs4 import BeautifulSoup

res = requests.get('https://movies.yahoo.com.tw/movie_thisweek.html')
for x in range(0, 9, 1):
    movie_name = BeautifulSoup(res.text).select('.release_movie_name .en')
    print(movie_name[x].text)
    movie_time = BeautifulSoup(res.text).select('.release_movie_time')
    print(movie_time[x].text)
    movie_level = BeautifulSoup(res.text).select('.leveltext span')
    print(movie_level[x].text)
    movie_count = BeautifulSoup(res.text).select('.leveltext .count span')
