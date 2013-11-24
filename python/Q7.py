import unittest
from itertools import islice
import functools
from lib.maths.primes import prime_sequence

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(list(islice(prime_sequence(),6)), [2,3,5,7,11,13])

if __name__ == '__main__':
    print(next(islice(prime_sequence(),10000,10001)))
    unittest.main()