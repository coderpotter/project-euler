from utils import *

"""
Find the sum of all the multiples of m or n below N.
"""

m, n, N = int(input("Enter m:")), int(input("Enter n:")), int(input("Enter N:"))

i, j, ans = m, n, 0
c = min(i, j)
while c < N:
    ans += c
    if c == i:
        i += m
    else:
        j += n
    c = min(i, j)
print(ans)