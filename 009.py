"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import functools
import operator


def pythagorean_triplets():
    c = 5
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if a ** 2 + b ** 2 == c ** 2:
                    yield a, b, c
        c += 1

for triplet in pythagorean_triplets():
    if sum(triplet) == 1000:
        print(functools.reduce(operator.mul, triplet))
        break
