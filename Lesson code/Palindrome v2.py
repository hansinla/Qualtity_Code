def is_palindromeV2(s):
    """(str)->bool

    This fundction should return True if
    and only if the string s is a palindrome.

    >>> is_palindromeV2('noon')
    True
    >>> is_palindromeV2('racecar')
    True
    >>> is_palindromeV2('dented')
    False

    """
    n = len(s)
    return s[:n//2] == reverse(s[n-n//2:])


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
