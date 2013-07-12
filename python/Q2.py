import unittest
import itertools

class Q2(unittest.TestCase):

    def setUp(self):
        # Setup
        pass

    def test_fib(self):
        # test code
        self.assertEqual(list(fib(7)), [1,1,2,3,5,8,13])

    def test_fibsUpTo(self):
        self.assertEqual(list(fibsUpTo(13)), [1,1,2,3,5,8,13])
        n = 100
        for x in fibsUpTo(n):
            self.assertTrue(x <= n)

    def test_evenFibsUpTo(self):
        n = 100
        for x in evenFibsUpTo(n):
            self.assertTrue(n % 2 == 0)


# CODE FROM HERE:
# Let's make some Generators!

def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield b
        a,b = b, a+b

def fibsUpTo(n):
    return itertools.takewhile(lambda x: x<=n, fib(n))

def evenFibsUpTo(n):
    return filter(lambda x: x % 2 == 0, fibsUpTo(n))


if __name__ == '__main__':
    print(sum(evenFibsUpTo(4*10**6)))
    unittest.main()
    

    
