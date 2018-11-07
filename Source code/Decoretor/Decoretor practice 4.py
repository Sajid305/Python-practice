
                
                # decoretor practice doc string return when function is caling

from functools import wraps
def decoretor(any_function):
    @wraps(any_function)
    def wrapper(*args,**kwargs):
        print(f"you are calling {any_function.__name__} function")
        print(f"{any_function.__doc__}")
        return any_function(*args,**kwargs)
    return wrapper


@ decoretor
def addition(a,b):
    '''this function take two number as argument and return there sum'''
    return a + b
print(addition(3,6))
