"""
What is the largest prime factor of the number N?
"""

N = int(input("Enter N: "))
n = N
ans = 0

while n % 2 == 0:
    n //= 2 # will never be a fractoin anyway
    ans = 2

# now n must be odd
for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
        n //= i # will never be a fractoin anyway
        ans = i

print(max(n, ans)) # in case n itself is a prime