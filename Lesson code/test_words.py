import unittest
import words

class TestWords(unittest.TestCase):

    def test_word_frequency(self):
        """ A dictionary with several items."""

        d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
        actual = words.word_frequency(d)
        expected = {'c': 2, 'b': 2, 'a': 1}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
