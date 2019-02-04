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
**"anime_search": searches for keyword (anime title) in a list of links and returns all that apply 
**"movie_search": searches for keyword (movie title) in a list of links and returns all that apply
**"source_finder": finds video source link and returns it
**"grab_episodes": gets episodes source link(value) and title(key) and return them as dictionary
'''


# Crawls watchcartoononline's dub anime list, returns title(key) and link(value) as dictionary
def dub_anime_crawl():
    animes = {}
    html = requests.get('https://www.thewatchcartoononline.tv/dubbed-anime-list')
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
    for lon_link in soup.find('div', {'class': 'ddmcc'}):
        link = lon_link.find_all('a')
        for href in link:
            hrlink = href.get('href')
            title = href.get('title')
            if hrlink is not None:
                animes[str(title)] = str(hrlink)
    return animes


# Crawls watchcartoononline's movie list, returns title(key) and link(value) as dictionary
def movie_crawl():
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
def sub_anime_crawl():
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
def cartoon_crawl():
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


# Crawls show url for the link of each episode, returns episode title(key) and episode link(value) as dictionary
def eps_napper(url):
    episodes = {}
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html5lib')
    for ep in soup.find_all("a", {"class": "sonra"}):
        title = ep.get("title")
        href = ep.get("href")
        episodes[str(title)] = str(href)
    return episodes
