class WordPlayStr(str):
    '''A special string class'''

    def same_start_and_end(self):
        '''(WordPlayStr)->bool

        >>> s = WordPlayStr('abracadabra')
        >>> s.same_start_and_end()
        True
        >>> s = WordPlayStr('canoe')
        >>> s.same_start_and_end()
        False
        '''

        return self[0] == self[-1]
     
if __name__ == '__main__':
    import doctest
    doctest.testmod()
