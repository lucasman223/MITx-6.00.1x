# -*- coding: utf-8 -*-
"""
exercise 2-3 Lucas Ma
In this problem, you'll create a program that guesses a 
secret number!

The program works as follows: you (the user) thinks of an 
integer between 0 (inclusive) and 100 (not inclusive). The 
computer makes guesses, and you give it input - is its 
guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!
"""

print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")
inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
low = 0
high = 100
ans = 50
while inp != "c":
    if inp == "l":
        low = ans
        ans = (low + high) // 2

    elif inp == "h":
        high = ans
        ans = (low + high) // 2
    else:
        print("Sorry, I did not understand your input.")
        
    print("Is your secret number", ans, "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret number was:", ans)



