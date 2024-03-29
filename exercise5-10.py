# -*- coding: utf-8 -*-
"""
Exercise 5-10 Lucas Ma
Write a generator, genPrimes, that returns the sequence of prime numbers 
on successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""

def genPrimes():
    prevPrimes = []
    x = 2
    isPrime = True
    while True:
        for p in prevPrimes:
            if (x % p) == 0:
                isPrime = False
                break
        
        if isPrime:
            prevPrimes.append(x)
            yield x
        x += 1
        isPrime = True

shift = 3
char = "z"
print(ord("a"))
print(chr( (ord(char) + shift - 97)%26 + 97 ))
