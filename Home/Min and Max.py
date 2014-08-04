"""
In this mission you should write you own py3 implementation of the built-in functions min and max. 
Some builtin functions are closed here: import, eval, exec, globals. 
Don't forget you should implement two functions in your code.
"""

def min(*args, **kwargs):
    print(args, kwargs, kwargs.get("key", None))
    if isinstance(args[0], (int, float, complex)):
        mini = args[0]
        for i in args:
            if i<mini:
                mini = i
        return mini


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    print (key,args,kwargs)
    return None

print (min([1, 2, 0, 3, 4]))