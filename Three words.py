"""
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
"""

def checkio(words):
    list = words.split()
    a=0
    b=False
    for i in list:
        if i.isalpha():
           a+=1
           if a>2:
               b = True
        else:
            a = 0
    return b

checkio("bla bla bla bla")