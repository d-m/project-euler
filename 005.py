"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import functools
import operator

# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800
# 1 * 2 * 3 * (2 * 2) * 5 * (2 * 3) * 7 * (2 * 2 * 2) * (3 * 3) * (2 * 5) = 3628800
# 1 * 2 * 2 * 2 * 3 * 3 * 5 * 7 = 2520
# lcm(a, b, c, ..., n)gcd(a, b, c, ..., n) = a * b * c * ... * n


def gcd(a, b):
    if b > a:
        x, y = b, a
    else:
        x, y = a, b
    
    if y == 0:
        return x
    else:
        _, r = x // y, x % y
        return gcd(y, r)


def lcm(a, b):
    return a * b // gcd(a, b)

print(functools.reduce(lcm, range(1, 21)))
