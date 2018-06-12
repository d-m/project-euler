"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

print(sum(number for number in range(1, 2000001) if is_prime(number)))