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
                print(x, p)
                isPrime = False
                break
        print(x, " ", isPrime)
        
        if isPrime:
            prevPrimes.append(x)
            yield x
        x += 1
        isPrime = True
     

