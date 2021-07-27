"""
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms. Assume that N will always be greater than 1.
"""

N = int(input("Enter N: "))
a, b, c = 1, 2, 3
ans = 0
while b < N:
    ans += b
    a = b + c
    b = a + c
    c = a + b
print(ans)
