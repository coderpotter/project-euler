"""
Find the product abc for a Pythagorean triplet for which a + b + c = N.
"""

N = int(input("Enter N: "))
for a in range(1, N - 2):
    for b in range(a + 1, N - 1):
        c = N - a - b
        if c ** 2 == a ** 2 + b ** 2:
            print(a, b, c, a * b * c)
