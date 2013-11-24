import unittest
import itertools
from functools import *
import operator

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(2640,sum_square_difference(10))

    # CODE FROM HERE:
    
def sum_square_difference(n):
    sumOfSquares = reduce(operator.add, map(lambda x: x*x, range(1,n+1)) )
    squareOfSums = reduce(operator.add, range(1,n+1)) ** 2
    return squareOfSums - sumOfSquares

if __name__ == '__main__':
    print(sum_square_difference(100))
    unittest.main()