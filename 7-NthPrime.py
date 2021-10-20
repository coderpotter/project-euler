"""
What is the Nth prime number?

Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
Estimate of Nth prime is approximately n (ln n + ln ln n - 1) (https://primes.utm.edu/howmany.html)
So, we'll check for primes less than n = N(logN + loglog(N-1)) + N
"""

import math, utils

N = int(input("Enter N: "))
print(utils.primesTillN(N + (N * int(math.log(N) + math.log(math.log(N)) - 1)))[N - 1])
