# -*- coding: utf-8 -*-
"""
Sandbox Problem Set 1 Lucas Ma
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels 
contained in the string s. Valid vowels are: 'a', 'e',
'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:
   
Number of vowels: 5
"""

def numVowels(s):
    answer = 0
    for char in s:
        if char in "aeiou":
            answer += 1
    
    return answer


