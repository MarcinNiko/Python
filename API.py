import omdb
from omdb import OMDBClient
import re
from datetime import datetime
import time

omdb.set_default('apikey',"81c13a05")
running = 1
i = 0
list_of_requests = []

#def functionToSort(list):
#     for i in list:
#        if re.fullmatch(type_of_sorting, i):
#            print(i)
#            return i


def sort_key(d):
    if type_of_sorting == "Rating":
        return d['imdb_rating']
    elif type_of_sorting == "Length":
        return d['runtime']
    elif type_of_sorting == "Release_date":
        return d['released']
    elif type_of_sorting == "Popularity":
        return d['imdb_votes']


while running:
    print("Podaj tytul/tytuly filmu")
    title = input()
    if title == "end":
        running = 0
        break
    if re.findall(r"[:]",title):
        word_list = title.split()
        type_of_sorting = word_list[-1]
        title = re.sub(type_of_sorting,'',title)
        type_of_sorting = type_of_sorting[1:]
    title_as_list = list(title.split(', '))
    for x in title_as_list:
        res = omdb.get(title=x)
        list_of_requests.append(res)
    list_of_requests.sort(key=sort_key, reverse=True)
    for y in list_of_requests:
        for key, value in list_of_requests[i].items():
            if key == "released" and value != "N/A":
                value = datetime.strptime(value, '%d %b %Y').strftime("%d.%m.%Y")
            print(f"{key}: {value}")
        i += 1
        print("\n")
    i = 0
    list_of_requests = []
