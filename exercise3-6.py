# -*- coding: utf-8 -*-
"""
exercise 3-6 Lucas Ma
We want to write some simple procedures that work on 
dictionaries to return information.

First, write a procedure, called how_many, which 
returns the sum of the number of values associated 
with a dictionary. For example:
    
>>> print(how_many(animals))
6
"""

def how_many(aDict):
    answer = 0
    for key in aDict:
        for i in aDict[key]:
            answer += 1
    return answer 



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(how_many(animals))


"""
This time, write a procedure, called biggest, which 
returns the key corresponding to the entry with the 
largest number of values associated with it. If 
there is more than one such entry, return any one 
of the matching keys.

Example usage:

>>> biggest(animals)
'd'
"""

def biggest(aDict):
    biggestKey = ""
    for key in aDict:
        length = len(aDict[key])
        if (biggestKey == ""):
            biggestKey = key
        elif length > len(aDict[biggestKey]):
            biggestKey = key
    
    return biggestKey

print(biggest(animals))