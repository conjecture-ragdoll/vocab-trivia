import unittest
from vocab_trivia import *
class Tests(unittest.TestCase):

    def test_cardinality6(self):
        self.assertEqual(len(words_with_root(random_root(), 18, 6)), 6)



if __name__ == '__main__':
    unittest.main()

