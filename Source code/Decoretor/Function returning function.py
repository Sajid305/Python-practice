
                # in this programm we are going to make a function that return a function

def function_that_return_a_function():
    def inner_function():
        print('this is returning inner function')
    return inner_function

my_function = function_that_return_a_function()
my_function()
# print(my_function())

# another function

def return_function(msg):
    def innerFunction(): #--> this inner function take a msg
        print(f" your message is {msg} ")
    return innerFunction
var = return_function('hello there')

var()