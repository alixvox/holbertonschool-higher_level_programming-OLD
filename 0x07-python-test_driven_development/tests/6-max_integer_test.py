#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer
    """
    test1 = [5, 7, 15, 2, 4]
    test2 = []
    test3 = ['ggb', 'bbc', 'cde']
    test4 = [[5, 6], [7, 8], [7, 5]]
    test5 = [('zeta', 'alpha'), ('echo', 'omnicron'), ('zeda', 'alpha')]
    test6 = [complex(5, 2), complex(10,7), complex(1,0)]

    def max_integer_test(self):
        self.assertEqual(max_integer(test1), 15)
        self.assertEqual(max_integer(test2), None)
        self.assertEqual(max_integer(test3), 'ggb')
        self.assertEqual(max_integer(test4), [7, 8])
        self.assertEqual(max_integer(test5), ('zeta', 'alpha'))
        with self.assertRaises(TypeError):
            max_integer(test7)

    if __name__ == '__main__':
        unittest.main()
