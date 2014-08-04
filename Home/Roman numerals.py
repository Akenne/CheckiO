"""
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The Roman numeral as a string.
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
"""

def swap(final, number, ch, num):
    final.append(ch)
    i = final.index(ch)
    final[i], final[i-1] = final[i-1], final[i]
    number += num
    return final,number

def checkio(number):
    final = []
    while number>=900:
        final.append('M')
        number -= 1000
    while number>=400 or number<0:
        if number < 0: 
            final, number = swap(final, number, 'C', 100)
            break
        final.append('D')
        number -= 500
    while number>=90:
        final.append('C')
        number -= 100
    while number>=40 or number<0:
        if number < 0: 
            final, number = swap(final, number, 'X', 10)
            break
        final.append('L')
        number -= 50
    while number>=9:
        final.append('X')
        number -= 10
    while number>=4 or number<0:
        if number < 0: 
            final, number = swap(final, number, 'I', 1)
            break
        final.append('V')
        number -= 5
    while number>0:
        final.append('I')
        number -= 1
    return (''.join(final)) 

checkio(3888)