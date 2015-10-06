def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    >>> num_buses(251)
    6
    """
    if n == 0:
        return 0
    else:
        if n%50 == 0:
            return int(n/50)
        else:
            return int(n/50)+1


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([-5,6,-10,8])
    (14, -15)
    >>> stock_price_summary([-5,-6,-7])
    (0, -18)
    """
    gains = 0
    losses = 0
    for change in price_changes:
        if change < 0:
            losses = losses + change
        else:
            gains = gains + change
    return (gains, losses)


def swap_k(L, k):
    """ (list) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = []
    >>> swap_k(nums, 0)
    >>> nums
    []
    >>> nums = [10,20]
    >>> swap_k(nums, 1)
    >>> nums
    [20, 10]
    >>> nums = [10,20,30]
    >>> swap_k(nums, 1)
    >>> nums
    [30, 20, 10]
    
    tempL=L[:k]
    tempR=L[-k:]
    for x in range(0,k):
        L.pop(0)
        L.pop()
    tempR.reverse()
    for item in tempR:
        L.insert(0, item)
    L.extend(tempL)
    """
    L[:k], L[-k:] = L[-k:], L[:k]

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
