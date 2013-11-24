import unittest
import itertools
from functools import reduce
import operator
from lib.maths.primes import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(17, sum_of_primes_below(10))

sum_of_primes_below = lambda n: reduce(operator.add, prime_sequence_up_to(n))

if __name__ == '__main__':
    print(sum_of_primes_below(2 * 10**6))
    unittest.main()