

        # having some problem with printing docstrings but i figerit out 

from functools import wraps
def decoretor(any_function):
    @wraps(any_function) # -->added wraps decoretor for returning doc string
    def wrapper(*args,**kwargs):
        ''' this is wrapper function '''
        print('yaaaaa i figure it out hehehe')
        return any_function(*args,**kwargs)
    return wrapper

@decoretor
def add(a,b):
    ''' this is add function '''
    return a+b

print(add(2,6))

print(add.__doc__)
