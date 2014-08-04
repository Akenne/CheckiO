"""
For language training our Robots want to learn about suffixes.
In this task, you are given a set of words in lower case. 
Check whether there is a pair of words, such that one word is the end of another (a suffix of another). 
For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.
"""

def checkio(words_set):
    if len(words_set) == 0:
        return False
    for a in words_set:
        for b in words_set:
            if a == b or len(a)<len(b):
                continue
            c = a[len(a)-len(b):len(a)]
            if c == b:
                return True
    return False

checkio({"helicopter", "li", "he"})