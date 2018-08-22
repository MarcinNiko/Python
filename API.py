import omdb
import re
from datetime import datetime
import os

omdb.set_default('apikey',"81c13a05")
running = 1
i = 0
list_of_requests = []
type_of_sorting = "No"
words_to_erase = ['5.1', '7.1', '5 1', '7 1', 'DUAL AUDIO', 'DUAL-AUDIO', 'MULTI-CHANNEL', 'Ita-Eng',
'2160p', '4K', '1080p', '720p', '480p', '360p', 'HD', 'FULL HD', 'FULLHD',
'x264', 'CH', 'X264', 'HEVC', 'DVD',
'WEB-DL', 'BrRip', 'Rip', 'DVDRip', 'XviD', 'BLURAY',
'EXTENDED', 'REMASTERED', 'DIRECTORS', 'UNRATED', 'AlTERNATE', '.avi', '.mkv']


def sort_key(d):
    if type_of_sorting == "Rating":
        return d['imdb_rating']
    elif type_of_sorting == "Length":
        return d['runtime']
    elif type_of_sorting == "Release_date":
        return d['released']
    elif type_of_sorting == "Popularity":
        return d['imdb_votes']


print("Press 1 if u want to load movies from file or 2 if u want to type names of the movies")
user_choice = input()
if user_choice == "1":
    list_of_requests = os.listdir('/Movies')
    list_of_titles = []
    for x in list_of_requests:
        for y in words_to_erase:
            x = x.replace(y, '')
        list_of_titles.append(x)
    print(list_of_titles)
    list_of_requests = []
    for x in list_of_titles:
        res = omdb.get(title=x)
        list_of_requests.append(res)
    for y in list_of_requests:
        for key, value in list_of_requests[i].items():
            if key == "released" and value != "N/A":
                value = datetime.strptime(value, '%d %b %Y').strftime("%d.%m.%Y")
            print(f"{key}: {value}")
        i += 1
        print("\n")
    i = 0
    list_of_requests = []
elif user_choice == "2":
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
            os.mkdir(f'/Movies/{x}')
            res = omdb.get(title=x)
            for char in res['imdb_votes']:
                if char in ",":
                    res['imdb_votes'] = res['imdb_votes'].replace(',', '')
            list_of_requests.append(res)
        if type_of_sorting != "No":
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
else:
    print("Wrong number pressed!")
