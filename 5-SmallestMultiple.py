"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to N?
Find LCM of multiple numbers
"""

import utils

N = int(input("Enter N: "))
print(utils.lcm(range(1, N + 1)))
