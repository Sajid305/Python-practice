
                        # defining a decoretors 


def decoretor(any_function):
    def wrapper(*args,**kwargs): #
        print('this is what you need extra')
        any_function(*args,**kwargs)
    return wrapper

# @decoretor we can add this but im not using this now
def function(i):
    print(f'your given number is {i} ')

function = decoretor(function)
function(5)

                                # another practice

# @decoretor we can add this but im not using this now
def add(a,b):
    return a + b

function = decoretor(add)
print(add(8,3))
