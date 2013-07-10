import unittest
import itertools
import math
import functools
class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_primeFactors(self):
        self.assertEqual(simplePrimeFactors(1755420849), [3,7,13,19,31,1213])
        

    def test_oneLinerPrimeFactor(self):
        self.assertEqual([], lambdaPrimeFactors(0)) # 0 is not prime, just empty list
        self.assertEqual([], lambdaPrimeFactors(1)) # 1 is not prime, just empty list
        self.assertEqual([2], lambdaPrimeFactors(2*2))
        self.assertEqual([2], lambdaPrimeFactors(2))
        self.assertEqual([2,3], lambdaPrimeFactors(2*2*3*3*3*3))
        self.assertEqual([2,3,5,7], lambdaPrimeFactors(2*2*3*3*3*5*7))
        

        #    
        #self.assertEqual(list(primeFactors(100)), list(lambdaPrimeFactors(100)))
        #self.assertFalse(True)

    def test_reduce(self):
        self.assertEqual(reduction(2,2), 1)
        self.assertEqual(reduction(5,5), 1)
        self.assertEqual(reduction(2*2*2*2*2*3,2), 3)
        self.assertEqual(reduction(2*2*2*2*2*7,2), 7)
        

    def test_largestPrimeFactor(self):
        pass
        #self.assertEqual(largestPrimeFactor(13195), 29)


    # CODE FROM HERE:
    # Could have try 2, and the rest the odd numbers in the range function... but oh well.


def simplePrimeFactors(n):
    for i in range(2,n):
        if(n%i==0):
            n = int(n/i)
            while( n % i == 0):
                n = n / i
            return [i] + simplePrimeFactors(int(n))
    return [n] if n > 1 else []

# Let's waste an hour on a hot wednesday to get a pure lambda version!
reduction = lambda n,i: list(itertools.takewhile(lambda tuple: tuple[1] == 0, 
                                map(divmod, itertools.repeat(n), 
                                        map(pow,itertools.repeat(i),itertools.count(1)))
                                    )
                            ) [-1][0]

lambdaPrimeFactors = lambda n : (
                        lambda nextFactor: 
                                [nextFactor] + lambdaPrimeFactors(
                                                                    # lambda function to reduce n by largest power of nextFactor 
                                                                    (lambda n,i: list(itertools.takewhile(lambda tuple: tuple[1] == 0, map(divmod, itertools.repeat(n), map(pow,itertools.repeat(i),itertools.count(1)))))[-1][0])
                                                                    (n, nextFactor)
                                                                )
                                )(  # Find the first prime factor, recurse.
                                filter(lambda factor : n % factor == 0, range(2, n+1)).__next__()
                                ) if n > 1 else []  

if __name__ == '__main__':
    lambdaPrimeFactors(600851475143)[-1]
    unittest.main()