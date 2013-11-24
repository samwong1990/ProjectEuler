import unittest
import itertools
import functools

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertEqual(3*4*5, product_of_pythagorean_triplet(12))
        
def product_of_pythagorean_triplet(n):
    for a in range(1, n-1):
        for b in range(1, n-1):
            c = n - a - b
            if(a*a + b*b == c*c):
                return a*b*c



if __name__ == '__main__':
    print(product_of_pythagorean_triplet(1000))
    unittest.main()