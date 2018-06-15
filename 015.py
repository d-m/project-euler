"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
import math


HEIGHT, WIDTH = 20, 20

def count_lattice_paths(x, y):
    # each path from one corner to the other requires x steps east plus y steps north
    n = x + y

    # of these n steps, we choose x of them of them to be north: n choose x
    return math.factorial(n) // (math.factorial(x) * math.factorial(y))

print(count_lattice_paths(20, 20))