"""
You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. 
Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.
Floating-point numbers are represented in computer hardware as base 2 (binary) fractions (read about this here). 
So we should check the result with ±0.001 precision.
"""

def checkio(*args):
    if len(args) == 0:
        return 0
    return max(args) - min(args)

def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3)