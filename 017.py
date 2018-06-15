"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

NUMBERS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def wordify(n):
    if 20 > n >= 0:
        return NUMBERS[n]
    elif 100 > n >= 20:
        tens, ones = divmod(n, 10)
        return ' '.join([NUMBERS[tens * 10], NUMBERS[ones]])
    elif 1000 > n >= 100:
        hundreds, remainder = divmod(n, 100)
        if remainder:
            remainder_words = wordify(remainder)
            return ' '.join([NUMBERS[hundreds], 'hundred and', remainder_words])
        return ' '.join([NUMBERS[hundreds], 'hundred'])
    elif n == 1000:
        return 'one thousand'

print(sum(len(wordify(number).replace(' ', '')) for number in range(1, 1001)))
