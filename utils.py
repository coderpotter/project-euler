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
