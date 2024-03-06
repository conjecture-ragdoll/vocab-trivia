import vocab_trivia

class VocabINFO:
    def __init__(self, min_length_word, word_count):
        self.lucky_word = vocab_trivia.select_word(min_length_word)
        self.choices = list({self.lucky_word} | vocab_trivia.words_with_root(vocab_trivia.other_root(self.lucky_word), min_length_word, word_count))
        self.lucky_definition = vocab_trivia.wikitionary_search(self.lucky_word)
        self.root_table = vocab_trivia.roots_in_word_list(self.lucky_word)
        
