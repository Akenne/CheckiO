"""
Sophia's drones are not soulless and stupid drones; they can make and have friends. 
In fact, they are already are working for the their own social network just for drones! 
Sophia has received the data about the connections between drones and she wants to know more about relations between them.
We have an array of straight connections between drones. 
Each connection is represented as a string with two names of friends separated by hyphen. 
For example: "dr101-mr99" means what the dr101 and mr99 are friends. 
Your should write a function that allow determine more complex connection between drones. 
You are given two names also. Try to determine if they are related through common bonds by any depth. 
For example: if two drones have a common friends or friends who have common friends and so on.
"""
#I did this wrong I think but it works
def check_connection(network, first, second):
    future = [first]
    visited = []
    dic = {}
    for i in network:
        a = i.split('-')
        if a[0] in dic and dic[a[0]] != a[1]:
            dic[a[0]].append(a[1])
        else:
            dic[a[0]] = [a[1]]
        if a[1] in dic and dic[a[1]] != a[0]:
            dic[a[1]].append(a[0])
        else:
            dic[a[1]] = [a[0]]
        if [a[0]] in dic.values():
            for key,val in dic.items():
                if a[1] == key:
                    break
                elif (''.join(ch for ch in val if ch.isalnum())) == str(a[0]):
                    dic[str(a[0])].append(key)
                    break  
    if first in dic:
        while len(future) > 0:
            for i in future:
                if i in visited:
                    future.remove(i)
                    continue
                else:
                    visited.append(i)
                for g in dic[i]:
                    if g == second:
                        return True
                    else:
                        if not g in visited:
                            future.append(g)
    return False

check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3")