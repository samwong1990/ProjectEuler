import unittest
import itertools

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isPalindrome(self):
        self.assertTrue(isPalindrome(''))
        self.assertTrue(isPalindrome(1))
        self.assertTrue(isPalindrome(101))
        self.assertTrue(isPalindrome(1001))
        self.assertTrue(isPalindrome(12321))

        self.assertFalse(isPalindrome(12))
        self.assertFalse(isPalindrome(1234))

    def test_largestPalindromProduct(self):
        self.assertEqual(9009, largestPalindromProduct(2))


    # CODE FROM HERE:

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largestPalindromProduct(digits):
    if(digits <= 0):
        return 0

    targetRange = range(10**(digits-1), 10**digits)
    catesianProducts = itertools.product(targetRange, repeat=2)
    return max(filter(isPalindrome, map(lambda tuple: tuple[0]*tuple[1],catesianProducts)))
    

if __name__ == '__main__':
    print(largestPalindromProduct(3))
    unittest.main()