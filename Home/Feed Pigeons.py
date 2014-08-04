"""
I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. 
Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, 
but in case there's not enough food for all the birds, the pigeons who arrived first ate first. 
Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, 
how many pigeons will be fed with at least one portion of wheat?
"""

def checkio(number):
    day = 1
    pidgeons = 0
    fed = 0
    while number>0:
        fed = pidgeons
        pidgeons += day
        if number<=pidgeons and number>fed:
            fed = number
        number = number - (pidgeons - fed) - fed
        day += 1
    return fed

checkio(10)