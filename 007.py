"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import math


def is_prime(number):
	if number <= 1:
		return False
	elif number <= 3:
		return True
	elif number % 2 == 0:
		return False
	else:
		for divisor in range(3, math.floor(math.sqrt(number)) + 1, 2):
			if number % divisor == 0:
				return False
		return True


def primes():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

for i, prime in enumerate(primes()):
    if i == 10000:
        print(prime)
        break