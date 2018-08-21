
def remove_chars(sentence):
    sentence = sentence[1:-1:1]
    return sentence

#string = remove_chars(str)

def return_half(sentence):
    sentence = sentence[:len(sentence)//2:1]
    return sentence

#string = return_half(str)

def change_value():
    word = "Hello World!"

    word_as_list = list(word)
    word_as_list[0] = 'M'

    word = ''.join(word_as_list)

    print(f"{word}")

#change_value()

def append_to_string(sentence):
    sentence_as_list = list(sentence)
    if len(sentence) >= 5:
        sentence_as_list.append("World")
    else:
        sentence_as_list.insert(0,"Welcome")

    sentence = ''.join(sentence_as_list)
    return sentence

#string = append_to_string(string)

def shortest_string(word, word_2):
    list_of_words = [word,word_2]
    output = min(x for x in list_of_words if isinstance(x, str))
    return output

#string = shortest_string("TAeto","Aelcome")

def filter_list(my_list):
    only_integers = [x for x in my_list if isinstance(x,int)]
    return  only_integers

#string = filter_list(my_list2)


def who_likes_it(list_of_likes):
    if len(list_of_likes) == 0:
        return ("no one likes this")
    elif len(list_of_likes) == 1:
        return (f"{list_of_likes[0]} likes this")
    elif len(list_of_likes) == 2:
        return (f"{list_of_likes[0]} and {list_of_likes[1]} like this")
    elif len(list_of_likes) == 3:
        return (f"{list_of_likes[0]}, {list_of_likes[1]} and {list_of_likes[2]} like this")
    else:
        return (f"{list_of_likes[0]}, {list_of_likes[1]} and {len(list_of_likes)-2} others like this")


assert who_likes_it([]) == "no one likes this", "Wrong like count!"
assert who_likes_it(["Ryszard"]) == "Ryszard likes this", "Wrong like count!"
assert who_likes_it(["Marcin", "Michal"]) == "Marcin and Michal like this", "Wrong like count!"
assert who_likes_it(["Edyta", "Igor", "Kamil"]) == "Edyta, Igor and Kamil like this", "Wrong like count!"
assert who_likes_it(["Michal", "Maciej", "Bartosz", "Przemek"]) == "Michal, Maciej and 2 others like this", "Wrong like count!"

