import requests
from bs4 import BeautifulSoup as bs
import time

def genius(a, b):
    # обработка входных данных
    artist = a
    artist = artist.strip()
    artist = [element.replace(' ', '-') for element in artist]
    artist = "".join(artist)

    song = b
    song = song.strip()
    song = [element.replace(' ', '-') for element in song]
    song = "".join(song)

    link = "https://genius.com" + '/' + artist + '-' + song + '-lyrics'

    api = requests.get(link)

    # if status_code == 200 then it works ok
    if api.status_code == 200:
        html = bs(api.text, 'html.parser')
        while True:
            try:
                html = html.find('div', class_='lyrics').text.split('\n')
                break
            except AttributeError:
                time.sleep(5)
                api = requests.get(link)
                html = bs(api.text, 'html.parser')
        print()
        string = ''
        for i in html:
            string += i + '\n'
        print(string)
        return string
    else:
        print('Something went wrong. (api code is ' + str(api.status_code) + ')')
