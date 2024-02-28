
import dearpygui.dearpygui as dpg
from vocab_trivia import *


'''
refer to:
 
https://dearpygui.readthedocs.io/en/latest/documentation/render-loop.html
'''

lucky_word = select_word(18)
lucky_definition = wikitionary_search(lucky_word)
similar_words = list(words_with_root(other_root(lucky_word), 18, 6))
root_list = roots_in_word_list(lucky_word)

dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text(lucky_definition)
    
    for x in range(len(similar_words)):
        dpg.add_button(label=similar_words[x], callback=lambda x: similar_words[x].trim() == lucky_word.trim(), user_data=similar_words[x])
    for x in range(len(root_list)):
        dpg.add_button(label=root_list[x], callback=root_definition, user_data=root_list[x])

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
