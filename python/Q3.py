import unittest
from itertools import *
import math
from functools import *
from lib.maths.primes import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_primeFactors(self):
        self.assertEqual(find_prime_factors(1755420849), [3,7,13,19,31,1213])
        

    def test_oneLinerPrimeFactor(self):
        self.assertEqual([], find_prime_factors(0)) # 0 is not prime, just empty list
        self.assertEqual([], find_prime_factors(1)) # 1 is not prime, just empty list
        self.assertEqual([2], find_prime_factors(2*2))
        self.assertEqual([2], find_prime_factors(2))
        self.assertEqual([2,3], find_prime_factors(2*2*3*3*3*3))
        self.assertEqual([2,3,5,7], find_prime_factors(2*2*3*3*3*5*7))
        self.assertEqual([2,5], find_prime_factors(50))
        
    def test_reduce(self):
        self.assertEqual(reduce_by_factor(2,2), 1)
        self.assertEqual(reduce_by_factor(5,5), 1)
        self.assertEqual(reduce_by_factor(2*2*2*2*2*3,2), 3)
        self.assertEqual(reduce_by_factor(2*2*2*2*2*7,2), 7)

if __name__ == '__main__':
    print(find_prime_factors(600851475143)[-1])
    unittest.main()