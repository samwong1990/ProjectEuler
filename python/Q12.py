import unittest
from itertools import *
from functools import *
import math
from lib.maths.primes import *
from lib.maths.factoring import *
from lib.functionalpy.functional import *


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTriangleNumberGenerator(self):
        self.assertEqual([1,3,6,10,15], list(islice(triangle_number_generator(), 5)))

    def testget_number_of_divisors(self):
        self.assertEqual([(1,1),(3,2),(6,4),(10,4),(15,4),(21,4),(28,6)],
            list(
                islice(
                    partial(map,introduce_number_of_factors_in_tuple)
                        (
                            triangle_number_generator()
                        )
                ,7)
                )
            )


def triangle_number_generator():
    sum = 0
    for x in count(1):
        sum += x
        yield sum


introduce_number_of_factors_in_tuple = lambda x: (x, len(find_factors_with_sympy(x)))
remove_those_with_less_than_n_factors = lambda n, fs: dropwhile(lambda ps: ps[1] <= n, fs)

def least_triangle_number_with_number_of_divisors_exceeding(n):
    return compose(
                    triangle_number_generator(),
                    partial(map,introduce_number_of_factors_in_tuple),
                    partial(dropwhile,lambda ps: ps[1] <= n),
                    partial(remove_those_with_less_than_n_factors, n),
                    partial(flip(islice),1),
                    list,
                    has_args=False
            )

if __name__ == '__main__':
    # Using a MacPro 2.3 GHz Core i5
    # Using my own vanilla factorization algorithm: 34.6s 
    # Using sympy's factorization algorithm: 2.3s
    print(least_triangle_number_with_number_of_divisors_exceeding(500))
    unittest.main()