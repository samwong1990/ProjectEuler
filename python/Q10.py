import unittest
import itertools
import functools
import Q7

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(17, sumOfPrimesBelow(10))
        

    # CODE FROM HERE:
def sumOfPrimesBelow(n):
    sum = 0
    for prime in Q7.gen_primes():
        if(prime >= n):
            break
        sum += prime
    return sum


if __name__ == '__main__':
    print(sumOfPrimesBelow(2000000))
    unittest.main()