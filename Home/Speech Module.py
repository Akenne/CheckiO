"""
Stephen's speech module is broken. This module is responsible for his number pronunciation. 
He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. 
Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. 
All the words in the string must be separated by exactly one space character. 
Be careful with spaces -- it's hard to see if you place two spaces instead one.
"""

def checkio(number):
    final= []
    if number >99:
        final.extend([FIRST_TEN[int((str(number))[0])-1], "hundred"]) 
    if 0<int((str(number))[-2:]) <10:
        final.append(FIRST_TEN[int((str(number))[-2:])-1])
    if 9<int((str(number))[-2:]) <20:
        final.append(SECOND_TEN[int((str(number))[-1:])])
    if 19<int((str(number))[-2:]):
        final.append(OTHER_TENS[int((str(number))[-2:-1])-2])
        if int((str(number))[-1:]) != 0:
            final.append(FIRST_TEN[int((str(number))[-1:])-1])
    return " ".join(final)

checkio(133)