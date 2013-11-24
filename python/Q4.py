import unittest
import itertools
import operator
from functools import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(1001))
        self.assertTrue(is_palindrome(12321))

        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(1234))

    def test_largest_palindrom_product(self):
        self.assertEqual(9009, largest_palindrom_product(2))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrom_product(digits):
    if(digits <= 0):
        return 0

    targetRange = range(10**(digits-1), 10**digits)
    catesianProducts = itertools.product(targetRange, repeat=2)
    tupleProduct = lambda t: reduce(operator.mul,t)
    return max(filter(is_palindrome, map(tupleProduct ,catesianProducts)))
    

if __name__ == '__main__':
    print(largest_palindrom_product(3))
    unittest.main()