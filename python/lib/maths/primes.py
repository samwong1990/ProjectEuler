from itertools import takewhile

def prime_sequence():
    """ Generate an infinite sequence of prime numbers.
    
    Sieve of Eratosthenes
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/

    Maps composites to primes witnessing their compositeness.
    This is memory efficient, as the sieve is not "run forward"
    indefinitely, but only as long as required by the current
    number being tested.
    """
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
            #print(D)

        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                #print("%d + %d = %d" % (p,q,p+q))
                D.setdefault(p + q, []).append(p)
            del D[q]
            #print(q)
            #print(D)

        q += 1 

reduce_by_factor = lambda n, i: reduce_by_factor(n//i, i) if n % i == 0 else n
prime_sequence_up_to = lambda n: takewhile(lambda p: p <= n, prime_sequence())

def find_prime_factors(n, unique=True, one_is_prime=False):
    factors = []
    if n < 1:
        return factors
    for prime in prime_sequence():
        if n == 1:
            if one_is_prime:
                factors = [1] + factors
            return factors
        while n % prime == 0:
            if not unique or not factors or factors[-1] is not prime:
                factors.append(prime)
            n = n//prime

