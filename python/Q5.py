import unittest
import itertools
import collections
import operator
from functools import *
from lib.maths.primes import find_prime_factors

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smallest_multiple_of(self):
        self.assertEqual(2520, smallest_multiple_of(10))

def smallest_multiple_of(n):
    """ Merge prime signature of range(1,n+1) to find the solution
    """
    listOfPrimeFactors = map(partial(find_prime_factors,unique=False), range(2,n+1))
    factorOccurences = collections.defaultdict(int)

    for x in listOfPrimeFactors:
        counts = collections.Counter(x)
        for primeFactor, occurences in counts.items():
            factorOccurences[primeFactor] = max(occurences, factorOccurences[primeFactor])

    return reduce(operator.mul, 
        map(lambda factor: factor[0] ** factor[1], factorOccurences.items()))
    
if __name__ == '__main__':
    print(smallest_multiple_of(20))
    unittest.main()