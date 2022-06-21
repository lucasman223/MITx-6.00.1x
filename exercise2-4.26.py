# -*- coding: utf-8 -*-
"""
Unit 2 problem 1 Lucas Ma
Write a function called polysum that takes 2 
arguments, n and s. This function should sum 
the area and square of the perimeter of the 
regular polygon. The function returns the sum, 
rounded to 4 decimal places.
"""

import math

def polysum(n,s):
    """
    

    Parameters
    ----------
    n : number of sides
        
    s : length of side
        

    Returns sum of area and square of the perimeter
    of regular polygon
    -------

    """
    area = (.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter**2,4)
    
print(polysum(18,36))
