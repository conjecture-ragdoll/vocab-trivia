# python3 vocab-trivia.py words_alpha.txt
import re
from nltk.corpus import wordnet
import requests
# word text file from https://github.com/dwyl/english-words
from PyDictionary import PyDictionary
import sys
import random
import pandas as pd
from py_thesaurus import Thesaurus
from bs4 import BeautifulSoup

dictionary = PyDictionary()

# Generate random link of certain root word by letter
root_link = 'https://en.m.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/'

# But ignore W and Y
possible_starting_letters = 'ABCDEFGHIJKLMNOPQRSTUVXZ'
random_letter = possible_starting_letters[random.randrange(0, 24)]

root_link_wLetter = root_link + random_letter

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

def valid_root_letter(character):
    return (character.isalpha() and character.islower())

def process_roots(root_str):
    roots = ''.join([x for x in root_str if valid_root_letter(x) or x == ","])
    root_list = re.split(",", roots)
    return root_list

def get_roots_by_letter(root_letter):
    roots = show_roots(root_link + root_letter.upper())
    root_list = map(process_roots, roots)
    return list(root_list)

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

def clickable_text():	#TODO: replaces clickable text with their definition and expands self defining words
    pass


def handle_definition(word_to_define, definitions):	# Ignore definitions that use the same word
    useable_defs = [x for x in definitions if word_to_define not in x]
    
    return useable_defs[0] if word_to_define not in useable_defs[0] else None

    

# Pick a random word, find definition
def wikitionary_search(word_to_define):
    url_str = 'http://en.wiktionary.org/wiki/' + word_to_define
    response = requests.get(url_str.replace('\n',''))

    print(response.status_code)    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ol = soup.find('ol')
        items = [item.text.strip() for item in ol.find_all('li')] if ol else []
        
        return handle_definition(word_to_define, items)    
    else:
        return None

# Parse the following root afterwards and generate another word that starts with it, if the steps fail then repeat previous step of generating a word that starts with root.

def roots_in_word_by_index(lucky_word, index): #TODO: Avoid w's or root letters not able to be scraped
    roots = [r for root in get_roots_by_letter(lucky_word[index]) for r in root]
    present_roots = [x for x in roots if x in lucky_word]
    return set(present_roots)

def roots_in_word(lucky_word):
    word = lucky_word.strip()
    present_roots = [roots_in_word_by_index(word, x) for x in range(len(word))]
    return present_roots

# Generate 6 words this way

# For roots that are parsed from words, find the definition to store in dict


# Display definition and display 6 words


# Display hint (reveals definition of a root)


# Penalty for incorrect guess


# Decrement score counter for hint


# Increment score counter for correct guess


# save score and repeat

rword = generate_rword(random_root(), 18)
print(rword)

print(wikitionary_search(rword))
print(roots_in_word(rword))
