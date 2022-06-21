# -*- coding: utf-8 -*-
"""
exercise 2-4.25 Lucas Ma
We can use the idea of bisection search to determine 
if a character is in a string, so long as the 
string is sorted in alphabetical order.

First, test the middle character of a string 
against the character you're looking for 
(the "test character"). If they are the same, 
we are done - we've found the character we're 
looking for!

If they're not the same, check if the test 
character is "smaller" than the middle 
character. If so, we need only consider the 
lower half of the string; otherwise, we only 
consider the upper half of the string. 
(Note that you can compare characters using 
 Python's < function.)

Implement the function isIn(char, aStr) which 
implements the above idea recursively to test 
if char is in aStr. char will be a single character 
and aStr will be a string that is in 
alphabetical order. The function should 
return a boolean value.
"""

def isIn(char, aStr):
    if (aStr == ""):
        return False
    test = aStr[len(aStr)//2]
    i = len(aStr)//2
    if test == char:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    else:
        if ord(char) < ord(test):
            return isIn(char, aStr[0:i])
        else:
            return isIn(char, aStr[i:])
        
print(isIn("d","abcde"))
print(isIn("d",""))
        
        
"""
more elegant TA answer
def isIn(c, s):
    if not s:
        return False
    m = len(s) // 2   
    if c < s[m]:
        return isIn(c, s[:m])
    elif c > s[m]:
        return isIn(c, s[m+1:])
    return True

should not 
"""        

