"""
author: DTT_Darkman
date started: Dec. 3, 2018
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
    html = requests.get('https://www.thewatchcartoononline.tv/dubbed-anime-list')
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
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
    html = requests.get('https://www.thewatchcartoononline.tv/movie-list')
    plain_text = html.text
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
    html = requests.get('https://www.thewatchcartoononline.tv/subbed-anime-list')
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
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
    html = requests.get('https://www.thewatchcartoononline.tv/cartoon-list')
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
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


# TODO needs threading
def source_finder(url):
    # Creating headless firefox browser
    ops = Options()
    ops.add_argument("--headless")
    pro = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(
        firefox_profile=pro,
        options=ops,
        executable_path="geckodriver.exe",
        firefox_binary="FirefoxPortable32\App\Firefox\\firefox.exe"
    )
    driver.implicitly_wait(10)

    # Getting page html source from url
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    driver.quit()
    print("Got soup, dinner time!")

    # Searching for "iframe" tag source link
    frame = soup.find("iframe", {"rel": "nofollow"})
    frame_src = frame.get("src")
    frame_url = "https://www.thewatchcartoononline.tv" + frame_src

    # Getting html from the iframe source link and getting video source link
    html = requests.get(frame_url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
    source = soup.find("source")
    link = source.get("src")
    print(link)
    return link





anime = movie_dic()
keys = dic_2_list(anime)
key = search(keys, "a bug's life")
print(key)
source_finder(anime[key])
