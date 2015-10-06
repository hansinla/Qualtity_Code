# test_swap_k.py 4/3/13

import a1
import unittest

class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_example1(self):
        '''Testing Boundaries & Size: an empty list first'''
        nums = []
        a1.swap_k(nums, 0)
        actual = nums
        expected = []
        self.assertEqual(actual, expected)

    def test_swap_example2(self):
        '''Testing Boundaries: the smallest list where the order can be changed'''
        nums = [10,20]
        a1.swap_k(nums, 1)
        actual = nums
        expected = [20, 10]
        self.assertEqual(actual, expected)

    def test_swap_example3(self):
        '''Testing Dichotomy: a list with an odd length'''
        nums = [10,20,30]
        a1.swap_k(nums, 1)
        actual = nums
        expected = [30, 20, 10]
        self.assertEqual(actual, expected)

    def test_swap_example4(self):
        '''Testing Size & Dichotomy: a large list with an even number of elements'''
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        actual = nums
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
