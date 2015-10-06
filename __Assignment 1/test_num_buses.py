# test_num_buses.py 4/3/13

import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_example1(self):
        '''Testing Boundaries & Size: zero passengers'''
        actual = a1.num_buses(0)
        expected = 0
        self.assertAlmostEqual(actual, expected)

    def test_num_buses_example2(self):
        '''Testing Boundaries & Size: filling exactly one bus'''
        actual = a1.num_buses(50)
        expected = 1
        self.assertAlmostEqual(actual, expected)

    def test_num_buses_example3(self):
        '''Testing Dichotomy & Boundary: an odd numbers of passengers'''
        actual = a1.num_buses(75)
        expected = 2
        self.assertAlmostEqual(actual, expected)

    def test_num_buses_example4(self):
        '''Testing Size: a large number of passengers'''
        actual = a1.num_buses(251)
        expected = 6
        self.assertAlmostEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
