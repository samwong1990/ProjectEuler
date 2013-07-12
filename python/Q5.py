import unittest
import itertools
import collections
import operator
import functools

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smallestMultiple(self):
        self.assertEqual(2520, smallestMultiple(10))

    # CODE FROM HERE:
    
lambdaPrimeFactors = lambda n : (
                        lambda nextFactor: 
                                [nextFactor] + lambdaPrimeFactors( int(n / nextFactor) )
                                )(  # Find the first prime factor, recurse.
                                filter(lambda factor : n % factor == 0, range(2, n+1)).__next__()
                                ) if n > 1 else []  

def smallestMultiple(n):
    listOfPrimeFactors = map(lambdaPrimeFactors, range(2,n+1))
    factorOccurences = collections.defaultdict(int)

    for x in listOfPrimeFactors:
        counts = collections.Counter(x)
        for primeFactor, occurences in counts.items():
            factorOccurences[primeFactor] = max(occurences, factorOccurences[primeFactor])

    return functools.reduce(operator.mul, 
        map(lambda factor: factor[0] ** factor[1], factorOccurences.items()))
    
if __name__ == '__main__':
    print(smallestMultiple(20))
    unittest.main()