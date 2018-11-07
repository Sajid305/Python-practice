


                     # Decoretors - enhance the functionality of other function
                    # @ use for decoretors

                # we are going to define some normal function first

def function1():
    print('this is function 1')

def function2():
    print('this is function 2')

                                    # making a decoretors for those normal function

def decoretors(any_function):
    def wrapper_function():
        print('i love you function')
        any_function()
    return wrapper_function

function1 = decoretors(function1)
function1()        


                                             # with syntactic sugar symbol

@decoretors
def function3():
    print('this is function 3')


@decoretors             # ----> shortcut way
def function4():
    print('this is function 4')

function3()             # ---> caling the function
function4()