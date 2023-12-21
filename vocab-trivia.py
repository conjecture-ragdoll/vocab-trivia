# python3 vocab-trivia.py words_alpha.txt
from nltk.corpus import wordnet

# word text file from https://github.com/dwyl/english-words
from PyDictionary import PyDictionary
import sys
import random
import pandas as pd
from py_thesaurus import Thesaurus


dictionary = PyDictionary()

# Generate random link of certain root word by letter
root_link = 'https://en.m.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/'

# But ignore W and Y
possible_starting_letters = 'ABCDEFGHIJKLMNOPQRSTUVXZ'
random_letter = possible_starting_letters[random.randrange(0, 24)]

root_link_wLetter = root_link + random_letter



#partials
# Pick a random root word
def show_roots(root_link_wLetter):
    table = pd.read_html(root_link_wLetter)
    return tuple(table[0]['Root'])

def show_root_meaning(root_link_wLetter):
    table = pd.read_html(root_link_wLetter)
    return tuple(table[0]['Meaning in English'])

def show_root_origin(root_link_wLetter):
    table = pd.read_html(root_link_wLetter)
    return tuple(table[0]['Origin language'])

def random_row_index(root_link_wLetter):
    roots = show_roots(root_link_wLetter)
    return random.randrange(0, len(roots))

def get_root(root_link_wLetter, index_val):
    return show_roots(root_link_wLetter)[index_val]

def valid_root(character):
    return (character.isalpha() and character.islower()) or character == '-'

def extract_root(root_str):     # selects random root from row
    roots = tuple(filter(None, ''.join([character for character in root_str if valid_root(character)]).split('-')))
    lucky_root = roots[random.randrange(0, len(roots))]
    return lucky_root

def get_root_meaning(root_link_wLetter, index_val):
    return show_root_meaning(root_link_wLetter)[index_val]

def get_root_origin(root_link_wLetter, index_val):
    return show_root_origin(root_link_wLetter)[index_val]

def random_root():
    return extract_root(get_root(root_link_wLetter, random_row_index(root_link_wLetter)))


# Generate a word that starts with the root

def search_txtfile(charseq):    # Search for a word that starts with a char sequence
    words = open(sys.argv[1])
    word_list = tuple(words.readlines())
    words.close()
    return tuple(word for word in word_list if charseq in word)  

def words_wmin_length(charseq, min_length):     # empty?
    words = search_txtfile(charseq)
    return tuple(word for word in words if len(word) >= int(min_length))

def find_longest(charseq, min_length):
    rwords = words_wmin_length(charseq, min_length)
    if rwords != ():
        return rwords
    if len(charseq) == min_length:
        return ()
    return find_longest(charseq, min_length - 1)

def generate_rword(root, min_length):   # TODO: watch out if there exists a min length with root word
    words = find_longest(root, min_length)
    if words == ():
        pass
    return words[random.randrange(len(words))]

# Pick a random word, find definition
def get_syns(lucky_word):
    return wordnet.synsets(lucky_word)

# Parse the following root afterwards and generate another word that starts with it, if the steps fail then repeat previous step of generating a word that starts with root.


# Generate 6 words this way
words6 = []

# For roots that are parsed from words, find the definition to store in dict


# Display definition and display 6 words


# Display hint (reveals definition of a root)


# Penalty for incorrect guess


# Decrement score counter for hint


# Increment score counter for correct guess


# save score and repeat

rword = generate_rword(random_root(), 13)
print(rword)

print(get_syns(rword))
