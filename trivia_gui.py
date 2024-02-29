
import dearpygui.dearpygui as dpg
from vocab_trivia import *


'''
refer to:
 
https://dearpygui.readthedocs.io/en/latest/documentation/render-loop.html
'''


def create_board(min_length, similar_words_max_length):
    global lucky_word, lucky_definition, similar_words, root_list
    lucky_word = select_word(min_length)
    lucky_definition = wikitionary_search(lucky_word)
    similar_words = list(words_with_root(other_root(lucky_word), min_length, similar_words_max_length))
    root_list = roots_in_word_list(lucky_word)


create_board(18, 6)

dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text(lucky_definition)
    
    for x in range(len(similar_words)):
        print(x)
        dpg.add_button(label=similar_words[x], callback=lambda a,b: create_board(18, 6) if a == b else print('wrong.'), user_data=[similar_words[x], lucky_word])
    for root in range(len(root_list)):
        dpg.add_button(label=root_list[root], callback=root_definition, user_data=root_list[root])

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
