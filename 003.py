"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math


def prime_factorization(n):
    primes = []
    number = n

    for divisor in range(2, math.floor(math.sqrt(number)) + 1):
        while number % divisor == 0:
            primes.append(divisor)
            number //= divisor

    return primes

print(prime_factorization(600851475143)[-1])