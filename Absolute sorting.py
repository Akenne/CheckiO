"""
Let's try some sorting. Here is an array with the specific rules.
The array (a tuple) has various numbers. 
You should sort it, but sort it by absolute value in ascending order. 
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). 
Your function should return the sorted list or tuple.
"""

def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

checkio((-20, -5, 10, 15))