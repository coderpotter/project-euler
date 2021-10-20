import math, functools, itertools


def is_palindrome(a):
    # takes 2 strings
    return a == a[::-1]


def list_product(L):
    # returns the product of a list
    return math.prod(L)


def lcm(L):
    # returns LCM of a list
    return functools.reduce(lambda a, b: a * b // math.gcd(a, b), L)


def combinations(L, x):
    # returns a list of all sets of x elements in a given list. Eg: L = [1, 2, 3] and x = 2, will return [(1, 2), (1, 3), (2, 3)]
    return itertools.combinations(L, x)


def isPrime(n):
    # returns True if n is prime, False otherwise. Any number < 2 is non-prime.
    if n % 2 and n != 2:
        i = 3
        while i <= n ** 0.5:
            if n % i == 0:
                return False
            i += 2
        return True
    return False


def primesTillN(n):
    # let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
    A = {_: True for _ in range(2, n + 1)}
    # for i = 2, 3, 4, ..., not exceeding √n do
    for i in range(2, int(n ** 0.5) + 1):
        # if A[i] is true
        if A[i]:
            # for j = ii, ii+i, ii+2i, ii+3i, ..., not exceeding n do
            #   A[j] := false
            __ = 0
            j = (i ** 2) + (__ * i)
            while j <= n:
                A[j] = False
                __ += 1
                j = (i ** 2) + (__ * i)
    return [ind for ind, b in A.items() if b]
