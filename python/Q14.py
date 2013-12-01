import pytest
from functools import lru_cache
import operator

""" Longest Collatz sequence under 1 million. Finishes in ~7s """


@pytest.mark.parametrize("input, expected", [(1, 1), (13, 10)])
def test_collatz(input, expected):
    assert collatz_length(input) is expected


def collatz_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1
    return


def next_collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


@lru_cache(maxsize=None)
def collatz_length(n):
    # print(collatz_length.cache_info())
    if n == 1:
        return 1
    return 1 + collatz_length(next_collatz(n))


def get_longest_collatz_chain_generator_under(n):
    """ Try from n // 2 to n + 1

    why n // 2?
        for k in range(1, n // 2)
            2k is even and collatz_length is 1 more than k
    """
    return max(
        enumerate(
            map(collatz_length, range(1, n + 1)),
            start=1),
        key=operator.itemgetter(1)
    )

print(get_longest_collatz_chain_generator_under(10 ** 6))
