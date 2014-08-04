"""
You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
 then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
"""

def checkio(array):
    a = len(array)
    sum = 0
    if a == 0:
        return 0
    for i in range(0,a,2):
        sum += array[i]
    sum *= array[a-1]
    return sum
    
checkio([1, 3, 5])