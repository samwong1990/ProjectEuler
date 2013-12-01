from lib.maths.primes import *
from itertools import *
from functools import *
from collections import Counter
import operator
import sys
sys.path.append("lib/sympy")
from sympy import *

def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    from python docs recipes
    http://docs.python.org/3.3/library/itertools.html
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

empty = lambda x: len(x) == 0

def find_factors(n):
	"""Returns all factors as a set.
	"""
	return set(map(
		partial(reduce,operator.mul), 
			dropwhile(
				empty, 
				powerset(find_prime_factors(n, one_is_prime=True, unique=False))
			)
		)
	)

def find_factors(n):
	"""Returns all factors as a set.
	"""
	return set(map(
		partial(reduce,operator.mul), 
			dropwhile(
				empty, 
				powerset(find_prime_factors(n, one_is_prime=True, unique=False))
			)
		)
	)

def find_factors_with_sympy(n):
	s = set(map(
		partial(reduce,operator.mul), 
			dropwhile(
				empty, 
				powerset(Counter(factorint(n)).elements())
			)
		)
	)
	s.add(1)
	return s

