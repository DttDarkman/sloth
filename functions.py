from crawlers import *
import difflib


dubbed = {}
subbed = {}
movies = {}
cartoons = {}
main_dic = {}
category = ""
dups = []
all_sear = False
dub_sear = False
sub_sear = False
mov_sear = False
cart_sear = False


def search_type(typ):
    global all_sear, dub_sear, sub_sear, mov_sear, cart_sear
    all_sear = False
    dub_sear = False
    sub_sear = False
    mov_sear = False
    cart_sear = False
    if typ == 1:
        all_sear = True
    if typ == 2:
        dub_sear = True
    if typ == 3:
        sub_sear = True
    if typ == 4:
        mov_sear = True
    if typ == 5:
        cart_sear = True

# Returns list sorted by relevance
def relevance_sort(keyword, lis):
    results = sorted(lis, key=lambda z: difflib.SequenceMatcher(None, z, str(keyword)).ratio(), reverse=True)
    return results


# Takes a list and a title(criter) and finds matching title in list and returns the keys for links in a list
def search(title_list, criteria):
    index = -1
    results = []
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
        nullAlert = "Sorry could not find {} in {}.".format(criteria, category)
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
    global category
    category = "dubbed"
    search_list = dic_2_list(dubbed)
    results = search(search_list, criteria)
    return results


# Searches thur subbed anime category
def search_sub(criteria):
    global category
    category = "subbed"
    search_list = dic_2_list(subbed)
    results = search(search_list, criteria)
    return results


# Searches thur movies category
def search_movies(criteria):
    global category
    category = "movies"
    search_list = dic_2_list(movies)
    results = search(search_list, criteria)
    return results


# Searches thur cartoons categories
def search_carts(criteria):
    global category
    category = "cartoons"
    search_list = dic_2_list(cartoons)
    results = search(search_list, criteria)
    return results


# Searches thur all categories
def search_all(criteria):
    results = []
    results.extend(search_carts(criteria))
    results.extend(search_dub(criteria))
    results.extend(search_sub(criteria))
    results.extend(search_movies(criteria))
    return results

# Takes dup keys in movies and adds "(Movie)" to the end of key
def dup_decoder():
    global movies
    for title in dups:
        dup_title = title
        for mov_title in movies:
            if mov_title == dup_title:
                new_key = f'{mov_title} (Movie)'
                movies[new_key] = movies.pop(mov_title)

# Finds all dup key "title" in movies
def dup_find():
    global dups
    diclis = [dubbed, subbed, cartoons]
    for dic in diclis:
        for key1 in dic.keys():
            for key2 in movies.keys():
                if key1 == key2:
                    dups.append(key1)

# Crawls all categories and returns them to global dictionaries
def startup():
    global dubbed, subbed, movies, cartoons, dups, main_dic
    dubbed = dub_anime_crawl()
    subbed = sub_anime_crawl()
    movies = movie_crawl()
    cartoons = cartoon_crawl()
    dup_find()
    dup_decoder()
    main_dic.update(dubbed)
    main_dic.update(subbed)
    main_dic.update(movies)
    main_dic.update(cartoons)
    


