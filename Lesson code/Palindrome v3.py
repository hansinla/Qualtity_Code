def is_palindromeV3(s):
    """(str)->bool

    This fundction should return True if
    and only if the string s is a palindrome.

    >>> is_palindromeV3('noon')
    True
    >>> is_palindromeV3('racecar')
    True
    >>> is_palindromeV3('dented')
    False

    """
    i = 0
    j = len(s)-1

    while i < j and s[i] == s[j]:
        i+=1
        j-=1

    return j <= i
