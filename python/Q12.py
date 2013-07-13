import unittest
import itertools
import functools
import math
import Q7

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTriangleNumberGenerator(self):
        self.assertEqual([1,3,6,10,15], list(itertools.islice(genTriangleNumber(), 5)))

    def testFindFactors(self):
        self.assertEqual([1], findFactors(1))
        self.assertEqual([1,3], findFactors(3))
        self.assertEqual([1,2,3,6], findFactors(6))
        self.assertEqual([1,2,4,7,14,28], findFactors(28))
        
    def testGetPrimesUpTo(self):
        self.assertEqual([2,3], getPrimesUpTo(3))
        self.assertEqual([2,3,5,7], getPrimesUpTo(8))
        self.assertEqual([2,3,5,7], getPrimesUpTo(7))
    
    def testGetNumOfDivisors(self):
        self.assertEqual(2, getNumOfDivisors(2))
        self.assertEqual(2, getNumOfDivisors(3))
        self.assertEqual(4, getNumOfDivisors(6))
        
    def test_method(self):
        self.assertEqual(1, naiveLeastTriangleNumberWithNDivisors(0))
        self.assertEqual(3, naiveLeastTriangleNumberWithNDivisors(1))
        self.assertEqual(6, naiveLeastTriangleNumberWithNDivisors(3))
        self.assertEqual(28, naiveLeastTriangleNumberWithNDivisors(5))
        


def genTriangleNumber():
    sum = 0
    for x in itertools.count(1):
        sum += x
        yield sum

primes = []
primeGenerator = Q7.gen_primes()
def getPrimesUpTo(n):
    if(len(primes) > 0 and primes[-1] > n):
        return list(itertools.takewhile(lambda x: x <= n, primes))
    else:
        # Ensure prime list is sufficiently long
        for x in primeGenerator:
            primes.append(x)
            if(x > n):
                break;
        # return the relevant slice
        return getPrimesUpTo(n)


def getNumOfDivisors(n):
    primeFactors = getPrimesUpTo(int(math.sqrt(n)+1))
    if( n == 1 ):
        return 1
    # if n is prime, divisors are 1 and n
    if(n == primeFactors[-1]):
        return 2 

    numberOfDivisors = 1
    for p in primeFactors:
        temp = n
        primeLargestExponent = 1
        while(temp % p == 0):
            temp /= p
            primeLargestExponent += 1
        numberOfDivisors *= primeLargestExponent
    return numberOfDivisors





factorsLookup = {1:[1]}
def findFactors(n):
    if(n in factorsLookup):
        return factorsLookup[n]
    factors = set([1,n])
    for factor in range(2, int(math.sqrt(n)+1)):
        quoRem = divmod(n,factor)
        if(quoRem[1] == 0):
            if(quoRem[0] in factorsLookup):
                factors.update(factorsLookup[quoRem[0]])
            else:
                factors.update(findFactors(quoRem[0]))
            if(factor in factorsLookup):
                factors.update(factorsLookup[factor])
            else:
                factors.update(findFactors(factor))
    factorsLookup[n] = list(factors)
    return factorsLookup[n]



def naiveLeastTriangleNumberWithNDivisors(n):
    for triNum in genTriangleNumber():
        print(triNum)

        if(len(findFactors(triNum)) > n):
            return triNum

def leastTriangleNumberWithNDivisors(n):
    for triNum in genTriangleNumber():
        print(triNum)
        if(getNumOfDivisors(triNum) > n):
            return triNum

if __name__ == '__main__':
    # Naive: <2mins
    # Optimized: 12s
    print(leastTriangleNumberWithNDivisors(500))
    unittest.main()