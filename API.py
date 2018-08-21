import omdb
from omdb import OMDBClient
import re
import json

omdb.set_default('apikey',"81c13a05")
running = 1
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
        print(x)
        res = omdb.get(title=x)
        for key, value in res.items():
            print(f"{key}: {value}")
        print("\n")

