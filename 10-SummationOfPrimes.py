"""
Find the sum of all the primes below two million.
"""

import utils

N = int(input("Enter N: "))
print(sum(utils.primesTillN(N)))
