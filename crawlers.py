"""
author: DTT_Darkman
date started: Dec. 3, 2018
"""

import requests
from bs4 import BeautifulSoup
''' 
       *******Needed functions******** 
**"web_crawlers": crawler watchcartoononline for each category "movies", "dubbed anime" and so on...
"anime_search": searches for keyword (anime title) in a list of links and returns all that apply 
"movie_search": searches for keyword (movie title) in a list of links and returns all that apply
"source_finder": finds video source link and returns it
"grab_episodes": gets episodes source link(value) and title(key) and return them as dictionary

'''


# Crawls watchcartoononline's dub anime list, returns title(key) and link(value) as dictionary
def dub_anime_dic():
    animes = {}
    html_code = requests.get('https://www.watchcartoononline.com/dubbed-anime-list')
    plain_text = html_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for lon_link in soup.find('div', {'class': 'ddmcc'}):
        print(lon_link)
        link = lon_link.find_all('a')
        for href in link:
            hrlink = href.get('href')
            title = href.get('title')
            if hrlink is not None:
                animes[str(title)] = str(hrlink)
    return animes


# Crawls watchcartoononline's movie list, returns title(key) and link(value) as dictionary
def movie_dic():
    movies = {}
    html_code = requests.get('https://www.watchcartoononline.com/movie-list')
    plain_text = html_code.text
    soup = BeautifulSoup(plain_text, 'html5lib')
    for lon_link in soup.find('div', {'class': 'ddmcc'}):
        link = lon_link.findAllNext('a')
        for href in link:
            hrlink = href.get('href')
            title = href.string
            if hrlink is not None:
                movies[str(title)] = str(hrlink)
    return movies


# Crawls watchcartoononline's subbed anime list, returns title(key) and link(value) as dictionary
def sub_anime_dic():
    sub_animes = {}
    html_code = requests.get('https://www.watchcartoononline.com/subbed-anime-list')
    plain_text = html_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for lon_link in soup.find('div', {'class': 'ddmcc'}):
        link = lon_link.find_all('a')
        for href in link:
            hrlink = href.get('href')
            title = href.get('title')
            if hrlink is not None:
                sub_animes[str(title)] = str(hrlink)
    return sub_animes


# Crawls watchcartoononline's cartoon list, returns title(key) and link(value) as dictionary
def cartoon_dic():
    cartoons = {}
    html_code = requests.get('https://www.watchcartoononline.com/cartoon-list')
    plain_text = html_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for lon_link in soup.find('div', {'class': 'ddmcc'}):
        link = lon_link.find_all('a')
        for href in link:
            hrlink = href.get('href')
            title = href.get('title')
            if hrlink is not None:
                cartoons[str(title)] = str(hrlink)
    return cartoons


# Takes a list and a title(criteria) and finds matching title in list and returns the key for link
def search(title_list, criteria):
    index = -1
    found = False
    # making all chars lowercase for criteria
    low_title_list = []
    low_criteria = criteria.lower()
    # making all chars lowercase for titles in list
    for title in title_list:
        low_title = title.lower()
        low_title_list.append(low_title)
    # Searching...
    for title in low_title_list:
        index += 1
        if title == low_criteria:
            found = True
            results = title_list[int(index)]
    if found is False:
        results = "Could Not Find {}. Sorry try again.".format(criteria)
    return results


# Takes dictionary and returns list of keys
def dic_2_list(dic):
    titles = []
    for key in dic:
        titles.append(key)
    return titles


def source_finder(url):
    pass



anime = movie_dic()
print(anime)


# titles = dic_2_list(anime)
# found = search(titles, "summer wars")
# print(found)
# found_link = anime[found]
# print(found_link)
