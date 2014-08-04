"""
You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
"""

def checkio(data):
    data1 = data[:]
    for a in data:
        c = 0
        for b in data:
            if a == b:
                c+=1
        if c<2:
            data1.remove(a)
    return data1

checkio([1, 2, 3, 1, 3])