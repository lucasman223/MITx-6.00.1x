"""
problem 2 Lucas Ma
Assume s is a string of lower case characters.

Write a program that prints the number of times 
the string 'bob' occurs in s. For example, if 
s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

answer = 0
inp = input("type in a string: ")
for i in range(len(inp) - 2):
    if inp[i] == "b" and inp[i+1] == "o" and inp[i+2] == "b":
        answer += 1

print("Number of times bob occurs is: ", answer)


