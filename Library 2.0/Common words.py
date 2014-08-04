"""
Let's continue examining words. You are given two string with words separated by commas. 
Try to find what is common between these strings. The words are not repeated in the same string.
Your function should find all of the words that appear in both strings. 
The result must be represented as a string of words separated by commas in alphabetic order.
"""

def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    c = []
    for a in first:
        for b in second:
            if a == b:
                c.append(a)
                break
                
    return ','.join(sorted(c))

checkio("hello,world", "hello,earth")