
                        # in this practice we are going to make our own function like map function

                                    # at first some old practice

list_ = list(range(1,11))
def square(l):
    return l**2

print(list(map(square,list_)))
# we can make this also with lambda function
# so we dont need to define this function 

list2 = list(range(1,11))
print(list(map(lambda l : l**2,list2)))

# now we are going to make our own function so that we dont need to use built in function

# making a function that take a function as a argument

list_3 = list(range(1,11))
def my_function(function,list_):
    new_list = []
    for item in list_:
        new_list.append(function(item))
    return new_list
print(my_function(square,list_))            # ---> i have use this square function from upper part of my programm

# we can also make this function with list comprehension function

list_4 = list(range(1,11))

def my_function2(function,list_):
    return [function(item) for item in list_]
print(my_function2(square,list_4))

# and now we have made a function who can take a function as a argument like map() function