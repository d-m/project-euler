"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math


def find_palindromes(minimum=100, maximum=999):
    
    def is_palindrome(number):
        string = str(number)
        return string == string[::-1]

    for i in range(minimum, maximum + 1):
        for j in range(minimum, maximum + 1):
            number = i * j
            if is_palindrome(number):
                yield number

print(max(find_palindromes()))
