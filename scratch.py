import re
import omdb

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


#assert who_likes_it([]) == "no one likes this", "Wrong like count!"
#assert who_likes_it(["Ryszard"]) == "Ryszard likes this", "Wrong like count!"
#assert who_likes_it(["Marcin", "Michal"]) == "Marcin and Michal like this", "Wrong like count!"
#assert who_likes_it(["Edyta", "Igor", "Kamil"]) == "Edyta, Igor and Kamil like this", "Wrong like count!"
#assert who_likes_it(["Michal", "Maciej", "Bartosz", "Przemek"]) == "Michal, Maciej and 2 others like this", "Wrong like count!"

def count_duplicates(sentence, how_many_times):
    sentence = [x for x in sentence if (sentence.count(x) == how_many_times)]
    output = ""
    for i in range(len(sentence)):
        if i%how_many_times == 0:
            output += sentence[i]
    return output

#string = count_duplicates("aabcdddee", 2)
#print(string)
#assert count_duplicates("aabcdddee", 2) == "ae", "Failed to count!" # only 'a' end 'e' were present 2 times.
#assert count_duplicates("indivisibility", 6) == "i", "Failed to count!"
#assert count_duplicates("Karima", 1) == "Krim", "Failed to count!"


names = {
    "Marcin": 1,
    "Patryk": 1,
    "Norbert": 0,
}

if "Michal" in names:
    names["Michal"] += 2
else:
    names["Michal"] = 2
#print(names)

names.pop("Norbert", None)
#print(names)


def word_counter(sentence):
    sentence_as_list = list(sentence.split(' '))
    output = {}
    for x in sentence_as_list:
        if  x.isalnum():
            if x in output:
                output[x] += 1
            else:
                output[x] = 1
        else:
            dot = x[len(x)-1:len(x)]
            x = x[0:len(x)-1]
            if x in output:
                output[x] += 1
            else:
                output[x] = 1
            if dot in output:
                output[dot] += 1
            else:
                output[dot] = 1
    return output

#string = word_counter("Ala ma kota. Ala ma psa.")
#print(string)

answer = {"Ala": 2, "ma": 2, "kota.": 1, "psa.": 1}
#assert word_counter("Ala ma kota. Ala ma psa.") == answer

def validatePIN(PIN):
    #return False if re.fullmatch("\d{4}",PIN) is None else True
    return bool(re.fullmatch("\d{4}",PIN))
#assert validatePIN("1234") == True, "Wrong validation!"
#assert validatePIN("12345") == False, "Wrong validation!"
#assert validatePIN("a234") == False, "Wrong validation!"


def validate_input(word):
    # Write a simple regex to validate a username. Allowed characters are:
    # lowercase letters, numbers, underscore
    # Length should be between 5 and 20 characters (both included).
    if (len(word) < 5 and len(word) > 20):  return False
    return False if (len(re.findall(r"[a-z_\d]", word)) != len(word)) is True else True


#assert validate_input("Summer Academmy") == False, "Bad validation!"
#assert validate_input("Summer_Academmy") == False, "Bad validation!"
#assert validate_input("summer_academmy") == True, "Bad validation!"


def valid_braces(sentence):
    if len(re.findall(r"[[]", sentence)) != len(re.findall(r"[]]", sentence))\
            or len(re.findall(r"[{]", sentence)) != len(re.findall(r"[}]", sentence))\
            or len(re.findall(r"[(]", sentence)) != len(re.findall(r"[)]", sentence)):
        return False
    else:
        return True



#assert valid_braces("(){}[]") == True, "Wrong answer!"
#assert valid_braces("([{}])") == True, "Wrong answer!"
#assert valid_braces("(}") == False, "Wrong answer!"
#assert valid_braces("[(])") == False, "Wrong answer!"
