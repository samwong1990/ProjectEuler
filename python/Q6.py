import unittest
import itertools
import functools

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(2640,sumSquareDifference(10))

    # CODE FROM HERE:
    
def sumSquareDifference(n):
    sumOfSquares = functools.reduce(lambda x,y:x+y, map(lambda x:x*x, range(1,n+1)))
    squareOfSums = functools.reduce(lambda x,y:x+y, range(1,n+1))
    squareOfSums *= squareOfSums
    return squareOfSums - sumOfSquares

if __name__ == '__main__':
    print(sumSquareDifference(100))
    unittest.main()