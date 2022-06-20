# -*- coding: utf-8 -*-
"""
problem 3 Lucas Ma
Assume s is a string of lower case characters.

Write a program that prints the longest substring 
of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program 
should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""


temp_ans = ""
ans = ""

inp = input("enter a string: ")
for char in inp:
    if len(temp_ans) == 0:
        temp_ans += char
    else:
        if ord(char) >= ord(temp_ans[-1]):
            temp_ans += char
        else:
            if len(temp_ans) > len(ans):
                ans = temp_ans
                temp_ans = char
            else:
                temp_ans = char

if len(temp_ans) > len(ans):
    ans = temp_ans

print("Longest substring in alphabetical order is:", ans)

    




