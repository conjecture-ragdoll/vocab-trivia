from pydictionary import Dictionary
import random
from wonderwords import RandomWord

# Generate random link of certain root word by letter
root_link = 'https://en.m.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/'

# But ignore W and Y
possible_starting_letters = 'ABCDEFGHIJKLMNOPQRSTUVXZ'
random_letter = possible_starting_letters[random.randrange(0, 24)]

root_link_wLetter = root_link + random_letter


# Pick a random root word
# Todo: webscraping

# Generate a word that starts with the root
dummy = 'de'

random_word = RandomWord()

rword = random_word.word(starts_with=dummy, word_min_length=12)

print(rword)
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