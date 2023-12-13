# python3 vocab-trivia.py words_alpha.txt

# word text file from https://github.com/dwyl/english-words
# from Pydictionary import Dictionary
import sys
import random
import pandas as pd


#dictionary = PyDictionary()

# Generate random link of certain root word by letter
root_link = 'https://en.m.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/'

# But ignore W and Y
possible_starting_letters = 'ABCDEFGHIJKLMNOPQRSTUVXZ'
random_letter = possible_starting_letters[random.randrange(0, 24)]

root_link_wLetter = root_link + random_letter


# Pick a random root word
def show_roots(root_link_wLetter, row):
    table = pd.read_html(root_link_wLetter)
    return tuple(table[0]['Root'])

def show_root_meaning(root_link_wLetter, row):
    table = pd.read_html(root_link_wLetter)
    return tuple(table[0]['Meaning in English'])

# Test print(len(show_roots(root_link_wLetter, 0)) == len(show_root_meaning(root_link_wLetter, 0)))



# Generate a word that starts with the root

def search_txtfile(charseq):    # Search for a word that starts with a char sequence
    words = open(sys.argv[1])
    word_list = tuple(words.readlines())
    return tuple(word for word in word_list if charseq in word)  

def words_wmin_length(charseq, min_length):
    return tuple(word for word in search_txtfile(charseq) if len(word) >= int(min_length))


def generate_rword(root, min_length):
    words = words_wmin_length(root, min_length)
    return words[random.randrange(len(words))]

print(generate_rword("anthro", 16))

# Parse the following root afterwards and generate another word that starts with it, if the steps fail then repeat previous step of generating a word that starts with root.


# Generate 6 words this way


# For roots that are parsed from words, find the definition to store in dict


# Pick a random word, find definition


# Display definition and display 6 words


# Display hint (reveals definition of a root)


# Penalty for incorrect guess


# Decrement score counter for hint


# Increment score counter for correct guess


# save score and repeat
