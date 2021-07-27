"""
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms. Assume that N will always be greater than 1.
"""
from tqdm import tqdm

N = int(input("Enter N: "))
a, b, c = 1, 2, 3
ans = b
for i in tqdm(range(1, (N + 1) // 3)):
    a = b + c
    b = a + c
    c = a + b
    ans += b
print(ans)
