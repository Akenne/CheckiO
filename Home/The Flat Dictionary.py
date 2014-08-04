"""
Python dictionaries are a convenient data type to store and process configurations. 
They allow you to store data by keys to create nested structures. 
You are given a dictionary where the keys are strings and the values are strings or dictionaries. 
The goal is flatten the dictionary, but save the structures in the keys. 
The result should be the a dictionary without the nested dictionaries. 
The keys should contain paths that contain the parent keys from the original dictionary. 
The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string ("").
"""

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if v == {}:
                v = ""
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    print (result)
    return result

flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    )