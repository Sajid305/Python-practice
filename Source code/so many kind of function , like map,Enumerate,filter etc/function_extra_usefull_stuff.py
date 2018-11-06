
                        # Doc string 

                    #''' this is doc string ''''

def func(a,b):
    ''' this is a doc string this function use tow argument and return addition of them'''
    return a+b
print(func(1,3))
print(func.__doc__) # ----> this is how we can check our doc string


# We can allso see doc string of built in function with the help of help() function

print(help(len))
print(help(max))        # -----> this is how we can use help function
print(help(type))
print(help(help))