# -*- coding: utf-8 -*-
"""
Problem 2 Lucas Ma
Now write a program that calculates the 
minimum fixed monthly payment needed in order 
pay off a credit card balance within 12 
months. By a fixed monthly payment, we mean 
a single number which does not change each 
month, but instead is a constant amount that 
will be paid each month.

In this problem, we will not be dealing with 
a minimum monthly payment rate.

The following variables contain values as 
described below:

balance - the outstanding balance on the 
credit card

annualInterestRate - annual interest rate 
as a decimal

The program should print out one line: the 
lowest monthly payment that will pay off all 
debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded 
monthly according to the balance at the end 
of the month (after the payment for that month is made). 
The monthly payment must be a multiple of 
$10 and is the same for all months. Notice 
that it is possible for the balance to 
become negative using this payment scheme, 
which is okay
"""
def amountNeededToPayDebt(balance, annualInterestRate):
    startingBalance = balance
    payment = 0
    while balance > 0:
        balance = startingBalance
        payment += 10
        for i in range(12):
            balance = balance - payment
            balance = balance + annualInterestRate/12*balance
    return "Lowest Payment: " + str(payment)

print(amountNeededToPayDebt(3926, .2))

