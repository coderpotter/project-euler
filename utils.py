import math

def swap(a, b):
    return b, a

def is_palindrome(a): # takes 2 strings
    return a == a[::-1]

def list_product(L): # returns the product of a list
    return math.prod(L)