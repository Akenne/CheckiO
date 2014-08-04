"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
"""

def checkio(number):
    sum = 1
    for i in range(len(str(number))):
        if int(str(number)[i]) == 0:
            continue
        sum *= int(str(number)[i])
    return sum

checkio(999)