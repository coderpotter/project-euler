"""
What is the Nth prime number?

Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
Estimate of Nth prime is approximately n (ln n + ln ln n - 1) (https://primes.utm.edu/howmany.html)
So, we'll check for primes less than n = N(logN + loglog(N-1)) + N
"""

import math

N = int(input("Enter N: "))
primes = []
n = N + (N * int(math.log(N) + math.log(math.log(N)) - 1))

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
primes = [ind for ind, b in A.items() if b]
print(primes[N - 1])
