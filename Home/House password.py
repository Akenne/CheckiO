"""
Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.
"""
#This code is gross sorry :(
def checkio(data):
    if len(data)<10:
        return False
    letter = False
    upper = False
    lower = False
    number = False
    for a in data:
        if a.isdigit():
            number = True
            break
    for a in data:
        if a.isupper():
            upper = True
            break
    for a in data:
        if a.islower():
            lower = True
            break
    for a in data:
        if a.isalpha():
            letter = True
            break
    for a in data:
        if not (a.isalpha() or a.isdigit()):
            return False
    if letter and upper and lower and number:
        return True
    return False

checkio('A1213pokl')