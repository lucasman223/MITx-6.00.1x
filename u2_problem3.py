# -*- coding: utf-8 -*-
"""
Problem 3 Lucas Ma
Write a program that uses these bounds and 
bisection search (for more info check out the 
Wikipedia page on bisection search) to find 
the smallest monthly payment to the cent (no 
more multiples of $10) such that we can pay 
off the debt within a year. Try it out with 
large inputs, and notice how fast it is (try 
the same large inputs in your solution to 
Problem 2 to compare!). Produce the same 
return value as you did in Problem 2.
"""

def bisSrchAmtNeeded(balance, annualInterestRate, low, high):
    payment = (low + high) / 2
    sBal = balance
    for i in range(12):
        balance = balance - payment
        balance = balance + annualInterestRate/12*balance
    
    if abs(balance) - 0.01 < 0:
        return round(payment, 2)
    
    elif balance < 0:
        balance = sBal
        return bisSrchAmtNeeded(balance, annualInterestRate, low, payment)
    else:
        balance = sBal
        return bisSrchAmtNeeded(balance, annualInterestRate, payment, high)
    
balance = 3298
annualInterestRate = .2
low = 0.01
high = balance
print("recursion", bisSrchAmtNeeded(3926, .2, low, high))


def bisSrchIteration(balance, annualInterestRate):
    low = 0.01
    high = balance
    sBal = balance
    while True:
        payment = (low + high) / 2
        balance = sBal
        for i in range(12):
            balance = balance - payment
            balance = balance + annualInterestRate/12*balance
        
        if abs(balance) - 0.01 < 0:
            return round(payment,2)
        elif balance < 0:
            high = payment
            
        else:
            low = payment
        

print("iteration", bisSrchIteration(3926, .2))            