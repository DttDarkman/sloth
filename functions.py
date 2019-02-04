from crawlers import *
import difflib


dubbed = {}
subbed = {}
movies = {}
cartoons = {}
dub_sear = False
sub_sear = False
mov_sear = False
cart_sear = False
results = []


def search_type(typ=None):
    global dub_sear, sub_sear, mov_sear, cart_sear
    dub_sear = False
    sub_sear = False
    mov_sear = False
    cart_sear = False
    if typ == "dubbed":
        dub_sear = True
    if typ == "subbed":
        sub_sear = True
    if typ == "movie":
        mov_sear = True
    if typ == "cartoon":
        cart_sear = True


# Crawls all categories and returns them to global dictionaries
def startup():
    global dubbed, subbed, movies, cartoons
    dubbed = dub_anime_crawl()
    subbed = sub_anime_crawl()
    movies = movie_crawl()
    cartoons = cartoon_crawl()


### ------ !!!FOR TESTING ONLY!!! ------ ###
def movie_get():
    global movies
    movies = movie_crawl()
### ------ !!!FOR TESTING ONLY!!! ------ ###


# Returns list sorted by relevance
def relevance_sort(keyword, lis):
    results = sorted(lis, key=lambda z: difflib.SequenceMatcher(None, z, str(keyword)).ratio(), reverse=True)
    return results


# Takes a list and a title(criter) and finds matching title in list and returns the keys for links in a list
def search(title_list, criteria):
    index = -1
    results = []
    low_results = []
    # making all chars lowercase for criter
    low_title_list = []
    low_criteria = criteria.lower()
    # making all chars lowercase for titles in list
    for title in title_list:
        low_title = title.lower()
        low_title_list.append(low_title)
    # Searching...
    for title in low_title_list:
        index += 1
        if title.find(low_criteria) != -1:
            results.append(title_list[int(index)])
    if len(results) <= 0:
        nullAlert = "Sorry could not find {}".format(criteria)
        results.append(nullAlert)
    return results


# Takes dictionary and returns list of keys
def dic_2_list(dic):
    titles = []
    for key in dic:
        titles.append(key)
    return titles


# Searches thur dubbed anime category
def search_dub(criteria):
    search_list = dic_2_list(dubbed)
    results = search(search_list, criteria)
    return results


# Searches thur subbed anime category
def search_sub(criteria):
    search_list = dic_2_list(subbed)
    results = search(search_list, criteria)
    return results


# Searches thur movies category
def search_movies(criteria):
    search_list = dic_2_list(movies)
    results = search(search_list, criteria)
    return results


# Searches thur cartoons categories
def search_carts(criteria):
    search_list = dic_2_list(cartoons)
    results = search(search_list, criteria)
    return results


# Searches thur all categories
def search_all(criteria):
    results = []
    search_list = []
    search_list.extend(search_carts(criteria))
    search_list.extend(search_dub(criteria))
    search_list.extend(search_sub(criteria))
    search_list.extend(search_movies(criteria))
    return results






















