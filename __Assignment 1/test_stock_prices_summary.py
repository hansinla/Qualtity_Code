# test_stock_prices_summary.py 4/3/13

import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stockPriceSum_example1(self):
        '''Testing Boundaries & Size: an empty list first'''
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stockPriceSum_example2(self):
        '''Testing Order; starting with a negative number'''
        actual = a1.stock_price_summary([-5,6,-10,8])
        expected = (14, -15)
        self.assertEqual(actual, expected)

    def test_stockPriceSum_example3(self):
        '''Testing Dichotomy: negative numbers only in a list with an odd length'''
        actual = a1.stock_price_summary([-5,-6,-7])
        expected = (0, -18)
        self.assertEqual(actual, expected)

    def test_stockPriceSum_example4(self):
        '''Testing Size: a large list'''
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
