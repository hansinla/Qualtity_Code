def is_palindromeV1(s):
    """(str)->bool

    This fundction should return True if
    and only if the string s is a palindrome.

    >>> is_palindromeV1('noon')
    True
    >>> is_palindromeV1('racecar')
    True
    >>> is_palindromeV1('dented')
    False

    """
    return reverse(s) == s


def reverse(s):
    """(str)->str

    Return a reversed version of string s

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''
    for ch in s:
        rev = ch + rev

    return rev
