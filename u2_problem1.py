# -*- coding: utf-8 -*-
"""
problem 1 Lucas Ma
Write a program to calculate the credit card 
balance after one year if a person only pays 
the minimum monthly payment required by the 
credit card company each month.

The following variables contain values as 
 below:

balance - the outstanding balance on the 
credit card

annualInterestRate - annual interest rate as 
a decimal

monthlyPaymentRate - minimum monthly payment 
rate as a decimal

For each month, calculate statements on the 
monthly payment and remaining balance. At the 
end of 12 months, print out the remaining 
balance. Be sure to print out no more than 
two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
So your program only prints out one thing: the 
remaining balance at the end of the year in 
the format:

Remaining balance: 4784.0
"""
def minPayment(balance, annualInterestRate, monthlyPaymentRate):
    
    for i in range(12):
        minPayment = monthlyPaymentRate*balance
        balance = balance - minPayment
        balance = balance + annualInterestRate/12*balance
    return "Remaining blanance: " + str(round(balance,2))

print(minPayment(484,0.2,.04))