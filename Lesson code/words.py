def word_frequency(letter_to_words):
    """ (dict of {str: list of str}) -> dict of {str: int}

    Precondition: the length of each list in letter_to_words is at least 1,
    each key in letter_to_words is a lowercase letter, and each value is a
    list of lowercase words beginning with that letter.

    Return a dictionary where the keys are the letters from letter_to_words,
    and the values are the number of words beginning with that letter in
    letter_to_words.

    >>> d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
    >>> word_frequency(d)
    {'a': 1, 'b': 2, 'c': 2}
    """

    newlist = {}
    for key in letter_to_words:
        newlist[key]=len(letter_to_words[key])
    return newlist

# d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
# print(word_frequency(d))
