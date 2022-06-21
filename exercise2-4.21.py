# -*- coding: utf-8 -*-
"""
exercise2-4.21 Lucas Ma
Write an iterative function, gcdIter(a, b), 
that implements this idea. One easy way to do 
this is to begin with a test value equal to 
the smaller of the two input arguments, and 
iteratively reduce this test value by 1 until
you either reach a case where the test divides 
both a and b without remainder, or you reach 
1.
"""
def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the 
    greatest common divisor of a & b.
    '''
    counter = min(a,b)
    answer = 1
    while counter >= 1:
        if a % counter == 0 and b % counter == 0:
            answer = counter
            break
        counter -= 1
    return answer

#tests
print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))

    

