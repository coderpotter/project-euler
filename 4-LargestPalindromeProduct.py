"""
Find the largest palindrome made from the product of two N-digit numbers.
"""

import utils

N = int(input("Enter N: "))

if N % 2:
    a, maxProd = 10 ** N - 1, [0, 0]
    while a > maxProd[1]:
        b = a
        while b > 10 ** (N - 1):
            ab = str(a * b)
            if utils.is_palindrome(ab):
                if utils.list_product([a, b]) > utils.list_product(maxProd):
                    maxProd = [a, b]
                break
            else:
                b -= 1
        a -= 1
    print(maxProd[0], maxProd[1], utils.list_product(maxProd))
else:
    print(10 ** N - 1, "9" * (N // 2) + "0" * (N // 2 - 1) + "1")
