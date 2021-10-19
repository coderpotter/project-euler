"""
Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.

(a+b+c)^2 = aa + bb + cc + 2ab + 2ac + 2bc
"""

import utils

N = int(input("Enter N: "))
print(2 * sum([utils.list_product(pair) for pair in utils.combinations(range(1, N + 1), 2)]))
